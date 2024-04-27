import time

from django.contrib.staticfiles.management.commands import (
    runserver,  # It plugs the static url when DEBUG is True
)
from django.core.management import call_command
from django.db import connections
from django.db.utils import OperationalError


class Command(runserver.Command):
    def add_arguments(self, parser):
        parser.add_argument(
            "--migrate",
            action="store_true",
            help="Migrate database before turning the server on.",
        )

        return super().add_arguments(parser)

    def handle(self, *args, **options):
        self.wait_database()

        if options["migrate"]:
            call_command("migrate")

        return super().handle(*args, **options)

    @staticmethod
    def wait_database() -> None:
        conn = None
        message_shown = False
        while conn is None:
            try:
                conn = connections["default"]
            except OperationalError:
                if not message_shown:
                    print("Waiting for database...")
                    message_shown = True
                time.sleep(1)
