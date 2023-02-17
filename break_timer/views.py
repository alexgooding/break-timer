from django.shortcuts import render
from break_timer.utils import convert_to_float, round_to_nearest_second, format_snooze_length
from django.db import transaction
from break_timer.models import MuteAudio
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'break_timer/home.html'

class TimerView(TemplateView):
    template_name = 'break_timer/timer.html'
    
    def post(self, request):
        work_length = convert_to_float(request.POST['work-length'])
        break_length = convert_to_float(request.POST['break-length'])
        rounded_work_length = round_to_nearest_second(work_length)
        rounded_break_length = round_to_nearest_second(break_length)
        rounded_work_snooze_length = round_to_nearest_second(work_length/5)
        rounded_break_snooze_length = round_to_nearest_second(break_length/5)
        formatted_work_snooze_length = format_snooze_length(rounded_work_snooze_length)
        formatted_break_snooze_length = format_snooze_length(rounded_break_snooze_length)

        data = {
            'work_length': rounded_work_length,
            'break_length': rounded_break_length,
            'work_snooze_length': rounded_work_snooze_length,
            'break_snooze_length': rounded_break_snooze_length,
            'formatted_work_snooze_length': formatted_work_snooze_length,
            'formatted_break_snooze_length': formatted_break_snooze_length
        }

        return self.render_to_response(data)

def mute(request):
    if request.method == 'POST':
        with transaction.atomic():
            mute_audio = MuteAudio.objects.get()
            updated_value = not mute_audio.mute
            mute_audio.mute = updated_value
            mute_audio.save()
        return HttpResponse(f"updated mute to {updated_value}")
    
    if request.method == 'GET':
        with transaction.atomic():
            mute = MuteAudio.objects.get().mute
        return HttpResponse(mute)
