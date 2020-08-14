from django.core.management.base import BaseCommand
from users import models as user_models
from django_seed import Seed


seeder = Seed.seeder()


class Command(BaseCommand):
    help = "seed Users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        repeat = int(options.get("number"))

        seeder.add_entity(
            user_models.User, repeat, {"is_staff": False, "is_superuser": False}
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{str(repeat)} of Users created"))
