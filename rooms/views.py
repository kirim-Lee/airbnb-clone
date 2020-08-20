from django.utils import timezone
from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator, EmptyPage
from django.views.generic.list import ListView


class HomeView(ListView):
    """ Home view definition """

    template_name = "rooms/home.html"
    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

