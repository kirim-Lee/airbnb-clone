from django.core.management.base import BaseCommand
from rooms import models as room_models
from users.models import User
from django_seed import Seed
import random

seeder = Seed.seeder()


class Command(BaseCommand):
    help = "Room seeder"

    def add_arguments(self, parser):

        return parser.add_argument("--number", help="how many rooms add", default=1)

    def handle(self, *args, **options):
        number = int(options.get("number"))

        all_users = User.objects.all()
        all_room_types = room_models.RoomType.objects.all()

        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.street_name(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_types),
                "price": lambda x: random.randint(10000, 500000),
                "beds": lambda x: random.randint(0, 10),
                "bedrooms": lambda x: random.randint(0, 10),
                "baths": lambda x: random.randint(0, 10),
                "guests": lambda x: random.randint(1, 20),
                "city": lambda x: seeder.faker.city(),
                "country": lambda x: seeder.faker.country(),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))

