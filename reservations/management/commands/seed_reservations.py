from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations.models import Reservation, STATUS_CHOICES
from users.models import User
from rooms.models import Room

import random
from datetime import date, timedelta

seeder = Seed.seeder()

check_in = date.today()

def get_random_check_in():
  global check_in
  today = date.today()
  random_day = random.randint(-30, 30)  
  check_in = today + timedelta(days= random_day)
  return check_in

def get_random_check_out():
  random_period = random.randint(1, 60)
  check_out = check_in + timedelta(days= random_period)
  return check_out

class Command(BaseCommand):
  help = "Reservation Seeder"

  def add_arguments(self, parser):
    return parser.add_argument("--number", help="how many reservations add", default=1)

  def handle(self, *args, **options):
    number = int(options.get('number'))

    users = User.objects.all()
    rooms = Room.objects.all()

    seeder.add_entity(Reservation, number, {
      "status": lambda x: random.choice(STATUS_CHOICES)[0],
      'check_in': lambda x: get_random_check_in(),
      'check_out': lambda x: get_random_check_out(),
      'guest':  lambda x: random.choice(users),
      'room': lambda x: random.choice(rooms)
    })
    seeder.execute()
    self.stdout.write(self.style.SUCCESS(f"{number} revervations created!"))
