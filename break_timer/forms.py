from django import forms
from django.core.exceptions import ValidationError
from break_timer.models import Timer

class TimerForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ('work_length', 'break_length')
    
    def clean_work_length(self):
        work_length = self.cleaned_data['work_length']
        if work_length <= 0 or work_length >= 6000:
            raise ValidationError('Work length value must be greater than 0 and less than 6000!')
        return work_length
    
    def clean_break_length(self):
        break_length = self.cleaned_data['break_length']
        if break_length <= 0 or break_length >= 6000:
            raise ValidationError('Break length value must be greater than 0 and less than 6000!')
        return break_length
