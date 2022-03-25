from django.urls import path
from break_timer import views

urlpatterns = [
    path("", views.home, name="home"),
    path("timer/", views.timer, name="timer")
]
