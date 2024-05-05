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

        expected_queries = re.findall(r"\d+\.\s[^\n\r]+", self.expected_queries, re.IGNORECASE)
        captured_queries = [f"{i}. {query['sql']}" for i, query in enumerate(self.captured_queries, start=1)]
        self.test_case.assertListEqual(captured_queries, expected_queries)


class TestCase(DjangoTestCase):
    def assertQueries(self, queries: str = "", func=None, *args, using=DEFAULT_DB_ALIAS, **kwargs):
        """
        Usage:
            with self.assertQueries(f\"""
                1. SELECT * FROM table_name WHERE id = {instance.id}
                2. SELECT * FROM another_table_name WHERE date = {timezone.now().date().isoformat()}::date
            \"""):
                # your code here

            To generate the expected queries, you can call this with an empty string, copy the "Captured queries were"
            text block and replace the values with your data.
        """
        conn = connections[using]

        context = AssertNumQueriesContext(self, queries, conn)
        if func is None:
            return context

        with context:
            func(*args, **kwargs)
