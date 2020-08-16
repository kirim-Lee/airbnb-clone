from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users.models import User
from rooms.models import Room

import random

seeder = Seed.seeder()

class Command(BaseCommand):
  help = "Review Seeder"

  def add_arguments(self, parser):
    return parser.add_argument("--number", help="how many reviews add", default=1)

  def handle(self, *args, **options):
    number = int(options.get('number'))

    users = User.objects.all()
    rooms = Room.objects.all()

    seeder.add_entity(Review, number, {
      'accuracy': lambda x: random.randint(0,5),
      'communication': lambda x: random.randint(0,5),
      'cleanliness': lambda x: random.randint(0,5),
      'location': lambda x: random.randint(0,5),
      'check_in': lambda x: random.randint(0,5),
      'value': lambda x: random.randint(0,5),
      'room': lambda x: random.choice(rooms),
      'user': lambda x: random.choice(users),
    })
    seeder.execute()
    self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
