from django.db import models
from django.contrib.auth.models import User


class Timer(models.Model):
    work_length = models.IntegerField()
    break_length = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timer')
