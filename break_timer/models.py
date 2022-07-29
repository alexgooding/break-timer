from django.db import models
from django.db import transaction


# Create your models here.
class MuteAudio(models.Model):
    mute = models.BooleanField(default=False)

# with transaction.atomic():
#     mute_audio = MuteAudio()
#     mute_audio.mute = True
#     mute_audio.save()
