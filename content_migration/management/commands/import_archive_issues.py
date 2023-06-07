from django.core.management.base import BaseCommand, CommandParser

from content_migration.management.import_archive_issues_handler import (
    handle_import_archive_issues,
)


class Command(BaseCommand):
    help = "Import Archive Issues from Drupal site"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--file", action="store", type=str)

    def handle(self, *args: tuple, **options: dict[str, str]) -> None:
        file_name = options["file"]

        handle_import_archive_issues(file_name)  # type: ignore

        self.stdout.write("All done!")