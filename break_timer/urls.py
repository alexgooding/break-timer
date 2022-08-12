from django.urls import path
from break_timer import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("timer/", views.timer, name="timer"),
    path("mute/", views.mute, name="mute")
]
