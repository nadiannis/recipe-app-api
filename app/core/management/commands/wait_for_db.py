"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        is_db_up = False

        while is_db_up is False:
            self.check(databases=['default'])
            is_db_up = True

        self.stdout.write(self.style.SUCCESS('Database available!'))
