from django.core.management.base import BaseCommand, CommandError
from ...news_sites import run_code


class Command(BaseCommand):
    help = "Scrapes data from the internet"

    def handle(self, *args, **options):
        try:
            run_code()

        except:
            print("Failed to run scrapper")
            return

        self.stdout.write(self.style.SUCCESS("Successfully printed all Book titles"))
        return