from django.core.management.base import BaseCommand
from django_seed import Seed
from lists.models import List
from users.models import User
from rooms.models import Room
from django.contrib.admin.utils import flatten

import random

seeder = Seed.seeder()

class Command(BaseCommand):
  help = "Lists Seeder"

  def add_arguments(self, parser):
    return parser.add_argument("--number", help="how many lists add", default=1)

  def handle(self, *args, **options):
    number = int(options.get('number'))

    users = User.objects.all()
    rooms = Room.objects.all()

    seeder.add_entity(List, number, {
     'user': lambda x: random.choice(users),
    })

    created = seeder.execute()
    cleaned = flatten(list(created.values()))
    
    for pk in cleaned:
      list_model = List.objects.get(pk=pk)
      to_add = rooms[random.randint(0,5): random.randint(6, len(rooms) + 1)]
      list_model.rooms.add(*to_add)

    self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
