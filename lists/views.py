from django.shortcuts import render, redirect, reverse
from . import models
from rooms import models as room_models

# Create your views here.
def save_room(request, room_pk):
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    if room is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favourite Houses"
        )
        the_list.rooms.add(room)
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))
