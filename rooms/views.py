from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator, EmptyPage

page_size = 10


def all_rooms(request):
    page = request.GET.get("page", default="1")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, page_size, orphans=3, allow_empty_first_page=True)

    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"rooms": rooms})

    except EmptyPage:
        return redirect("/")
