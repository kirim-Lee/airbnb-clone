from django.core.management.base import BaseCommand
from rooms import models as room_models
from django_seed import Seed

seeder = Seed.seeder()


class Command(BaseCommand):

    help = "규칙"

    # def add_arguments(self, parser):
    #     return parser.add_argument("--times", help="How many")

    def handle(self, *args, **options):
        seeder.add_entity(room_models.HouseRule, 10)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"HouseRules created!"))
