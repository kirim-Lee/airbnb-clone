from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

page_size = 10


def all_rooms(request):
    page = request.GET.get("page", default="1")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, page_size)
    rooms = paginator.get_page(page)

    return render(request, "rooms/home.html", {"rooms": rooms})
