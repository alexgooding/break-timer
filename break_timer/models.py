from django.db import models


# Create your models here.
class MuteAudio(models.Model):
    mute = models.BooleanField(default=False)

