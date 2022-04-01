from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'break_timer/home.html')

def timer(request):
    if request.method == 'POST':
        work_length = request.POST['work-length']
        break_length = request.POST['break-length']
        data = {
            'work_length': work_length,
            'break_length': break_length,
            'work_snooze_length': float(work_length)/5,
            'break_snooze_length': float(break_length)/5
        }
        return render(request, 'break_timer/timer.html', data)
