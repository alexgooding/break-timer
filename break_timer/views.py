from break_timer.utils import round_to_nearest_second, format_snooze_length
from break_timer.models import Timer
from break_timer.forms import TimerForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

class SignupView(UserPassesTestMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/home'

    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('home')

class LoginScreenView(LoginView):
    template_name = 'login.html'

class LogoutScreenView(LogoutView):
    template_name = 'logout.html'

class HomeView(LoginRequiredMixin, CreateView):
    template_name = 'home.html'
    model = Timer
    form_class = TimerForm
    success_url = '/timer'
    login_url = reverse_lazy('login')

    # Inject current user into model data before saving the form
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    # Set default values for the form
    def get_initial(self):
        initial = super().get_initial()
        try:
            latest_timer = Timer.objects.filter(user_id=self.request.user.id).latest('created')
            initial['work_length'] = latest_timer.work_length
            initial['break_length'] = latest_timer.break_length
        except Timer.DoesNotExist:
            initial['work_length'] = 25
            initial['break_length'] = 5
        return initial

class TimerView(LoginRequiredMixin, TemplateView):
    template_name = 'timer.html'
    login_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_timer = Timer.objects.filter(user_id=self.request.user.id).latest('created')
        rounded_work_length = round_to_nearest_second(latest_timer.work_length)
        rounded_break_length = round_to_nearest_second(latest_timer.break_length)
        rounded_work_snooze_length = round_to_nearest_second(latest_timer.work_length/5)
        rounded_break_snooze_length = round_to_nearest_second(latest_timer.break_length/5)
        formatted_work_snooze_length = format_snooze_length(rounded_work_snooze_length)
        formatted_break_snooze_length = format_snooze_length(rounded_break_snooze_length)

        context.update({
            'work_length': rounded_work_length,
            'break_length': rounded_break_length,
            'work_snooze_length': rounded_work_snooze_length,
            'break_snooze_length': rounded_break_snooze_length,
            'formatted_work_snooze_length': formatted_work_snooze_length,
            'formatted_break_snooze_length': formatted_break_snooze_length
        })

        return context   

class ToggleMuteView(View):
    def post(self, request):
        request.session['mute_state'] = request.POST.get('mute_state')
        return HttpResponse(f"Session {'muted' if request.POST.get('mute_state') == 'true' else 'unmuted'}")
