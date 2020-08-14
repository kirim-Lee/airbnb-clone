from django.core.management.base import BaseCommand
from rooms import models as room_models
from users.models import User
from django_seed import Seed
import random
from django.contrib.admin.utils import flatten

seeder = Seed.seeder()


def add_random(room, types):
    for t in types:
        magic_number = random.randint(0, 15)
        if magic_number % 3 == 0:
            room.add(t)


class Command(BaseCommand):
    help = "Room seeder"

    def add_arguments(self, parser):

        return parser.add_argument("--number", help="how many rooms add", default=1)

    def handle(self, *args, **options):
        number = int(options.get("number"))

        all_users = User.objects.all()
        all_room_types = room_models.RoomType.objects.all()
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

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

        # photo
        created = seeder.execute()
        created_clean = flatten(list(created.values()))

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(1, random.randint(3, 5)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/rooms/photos_seed/{random.randint(1,31)}.webp",
                    room=room,
                )

            add_random(room.amenity, amenities)
            add_random(room.facility, facilities)
            add_random(room.house_rules, rules)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))

