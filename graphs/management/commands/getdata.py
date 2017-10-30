from django.core.management.base import BaseCommand, CommandError
from graphs.get_data import getComedFiveMinFeed

class Command(BaseCommand):
    help = 'Update COMED data'

    def handle(self, *args, **kwargs):
        getComedFiveMinFeed()
        print("COMED Updated")