import re

from django.db import DEFAULT_DB_ALIAS, connections
from django.test import TestCase as DjangoTestCase
from django.test.testcases import CaptureQueriesContext


class AssertNumQueriesContext(CaptureQueriesContext):
    def __init__(self, test_case: DjangoTestCase, queries: str, connection):
        self.test_case = test_case
        self.expected_queries = queries
        super().__init__(connection)

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
