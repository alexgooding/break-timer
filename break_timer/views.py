from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'break_timer/home.html')

def timer(request):
    return render(request, 'break_timer/timer.html')
