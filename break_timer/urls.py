from django.urls import path
from break_timer import views

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginScreenView.as_view(), name="login"),
    path("logout/", views.LogoutScreenView.as_view(), name="logout"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("timer/", views.TimerView.as_view(), name="timer"),
    path("mute/", views.ToggleMuteView.as_view(), name="mute"),
]
