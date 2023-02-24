from django.db import models
from django.contrib.auth.models import User


class Timer(models.Model):
    work_length = models.DecimalField(decimal_places=1, max_digits=5)
    break_length = models.DecimalField(decimal_places=1, max_digits=5)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timer')
