from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(
        room_list, 10, orphans=5
    )  # orphans -> 다음 페이지에 5개보다 적은 object들이 있다면 전페이지에 넣어라
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/home.html",
            context={"page": rooms},
        )
    except EmptyPage:
        return redirect("/")
