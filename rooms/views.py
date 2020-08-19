from django.shortcuts import render
from . import models
import math

page_size = 10


def all_rooms(request):
    query = request.GET
    page = int(query.get("page", default="1") or "1")

    offset = (page - 1) * page_size
    limit = page * page_size

    rooms = models.Room.objects.all()[offset:limit]
    page_count = math.ceil(models.Room.objects.count() / page_size)
    return render(
        request,
        "rooms/home.html",
        {"rooms": rooms, "page": page, "page_count": page_count,},
    )
