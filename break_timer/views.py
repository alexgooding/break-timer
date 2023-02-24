from break_timer.utils import convert_to_float, round_to_nearest_second, format_snooze_length
from break_timer.models import Timer
from break_timer.forms import TimerForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, CreateView

class HomeView(CreateView):
    template_name = 'home.html'
    model = Timer
    form_class = TimerForm
    success_url = '/timer/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class TimerView(TemplateView):
    template_name = 'timer.html'
    
    latest_timer = Timer.objects.latest('created')
    rounded_work_length = round_to_nearest_second(latest_timer.work_length)
    rounded_break_length = round_to_nearest_second(latest_timer.break_length)
    rounded_work_snooze_length = round_to_nearest_second(latest_timer.work_length/5)
    rounded_break_snooze_length = round_to_nearest_second(latest_timer.break_length/5)
    formatted_work_snooze_length = format_snooze_length(rounded_work_snooze_length)
    formatted_break_snooze_length = format_snooze_length(rounded_break_snooze_length)

    extra_context = {
        'work_length': rounded_work_length,
        'break_length': rounded_break_length,
        'work_snooze_length': rounded_work_snooze_length,
        'break_snooze_length': rounded_break_snooze_length,
        'formatted_work_snooze_length': formatted_work_snooze_length,
        'formatted_break_snooze_length': formatted_break_snooze_length
    }   

class ToggleMuteView(View):
    def post(self, request):
        request.session['mute_state'] = request.POST.get('mute_state')
        return HttpResponse(f"Session {'muted' if request.POST.get('mute_state') == 'true' else 'unmuted'}")
