from django.shortcuts import render


def all_rooms(request):
    return render(request, "index.html", {"hello": "hi, now"})
