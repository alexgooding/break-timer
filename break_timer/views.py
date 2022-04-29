from django.shortcuts import render
from django.http import HttpResponse
from utils import round_to_nearest_second

def home(request):
    return render(request, 'break_timer/home.html')

def timer(request):
    if request.method == 'POST':
        work_length = request.POST['work-length']
        break_length = request.POST['break-length']
        rounded_work_length = round_to_nearest_second(work_length)
        rounded_break_length = round_to_nearest_second(break_length)
        rounded_work_snooze_length = round_to_nearest_second(work_length/5)
        rounded_break_snooze_length = round_to_nearest_second(break_length/5)
        data = {
            'work_length': rounded_work_length,
            'break_length': rounded_break_length,
            'work_snooze_length': rounded_work_snooze_length,
            'break_snooze_length': rounded_break_snooze_length
        }
        return render(request, 'break_timer/timer.html', data)

