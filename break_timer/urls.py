from django.urls import path
from break_timer import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("timer/", views.TimerView.as_view(), name="timer"),
    path("mute/", views.ToggleMuteView.as_view(), name="mute"),
]
