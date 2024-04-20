import json
import re

from django.db import DEFAULT_DB_ALIAS, connections
from django.test import TestCase as DjangoTestCase
from django.test.testcases import CaptureQueriesContext, _AssertNumQueriesContext
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.test import APITestCase as DRFAPITestCase


def extract_response_data(response: Response):
    if not hasattr(response, "data"):
        return response.content
    return json.loads(JSONRenderer().render(response.data))


class AssertNumQueriesContext(_AssertNumQueriesContext):
    def __init__(self, test_case: DjangoTestCase, queries: str, connection):
        self.test_case = test_case
        self.expected_queries = queries
        super(CaptureQueriesContext, self).__init__(connection)

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        if exc_type is not None:
            return

        expected = len(re.findall(r"\d+\.\s", self.expected_queries, re.IGNORECASE))
        executed = len(self.captured_queries)
        captured_queries_str = "\n".join(
            f"{i}. {query['sql']}" for i, query in enumerate(self.captured_queries, start=1)
        )
        self.test_case.assertEqual(
            executed,
            expected,
            f"{executed} queries executed, {expected} expected\nCaptured queries were:\n{captured_queries_str}",
        )


class TestCase(DjangoTestCase):
    def assertQueries(self, queries: str = "", func=None, *args, using=DEFAULT_DB_ALIAS, **kwargs):
        """
        Usage:
            with self.assertQueries(\"""
                1. SELECT * FROM table_name
                2. SELECT * FROM another_table_name
            \"""):
                # your code here

            To generate the expected queries, you can just call it empty and copy the "Captured queries were" text block
        """
        conn = connections[using]

        context = AssertNumQueriesContext(self, queries, conn)
        if func is None:
            return context

        with context:
            func(*args, **kwargs)


class APITestCase(DRFAPITestCase):
    def assertResponse(self, response: Response, status_code: int, expected_data) -> None:
        self.assertListEqual(
            [response.status_code, extract_response_data(response)],
            [status_code, expected_data],
        )

    def assertNotFoundResponse(self, response: Response, message: str | None = None) -> None:
        self.assertResponse(response, status.HTTP_404_NOT_FOUND, {"detail": message or "Not found."})

    def assertUnauthorizedResponse(self, response: Response, expected_data: dict | None = None) -> None:
        data = expected_data or {"detail": "Authentication credentials were not provided."}
        self.assertResponse(response, status.HTTP_401_UNAUTHORIZED, data)

    def assertBadRequestResponse(self, response: Response, expected_data: dict) -> None:
        self.assertResponse(response, status.HTTP_400_BAD_REQUEST, expected_data)

    def assertOkResponse(self, response: Response, expected_data: list | dict | None) -> None:
        self.assertResponse(response, status.HTTP_200_OK, expected_data)

    def assertCreatedResponse(self, response: Response, expected_data: dict) -> None:
        self.assertResponse(response, status.HTTP_201_CREATED, expected_data)

    def assertForbiddenResponse(self, response: Response, message: str | None = None) -> None:
        message = message or "You do not have permission to perform this action."
        self.assertResponse(response, status.HTTP_403_FORBIDDEN, {"detail": message})

    def assertNoContentResponse(self, response: Response) -> None:
        self.assertResponse(response, status.HTTP_204_NO_CONTENT, None)
