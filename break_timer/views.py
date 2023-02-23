from django.shortcuts import render
from break_timer.utils import convert_to_float, round_to_nearest_second, format_snooze_length
from django.db import transaction
from break_timer.models import MuteAudio
from django.http import HttpResponse
from django.views.generic import View, TemplateView, FormView

class HomeView(TemplateView):
    template_name = 'home.html'

class TimerView(TemplateView):
    template_name = 'timer.html'
    
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

class ToggleMuteView(View):
    def post(self, request):
        request.session['mute_state'] = request.POST.get('mute_state')
        return HttpResponse(f"Session {'muted' if request.POST.get('mute_state') == 'true' else 'unmuted'}")
