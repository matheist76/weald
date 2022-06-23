from .traits import Options, Equipment, RoguishFeats, Connections, BgQuestions, BgAnswers, Moves, WeaponSkills, Ranges, Natures, Drives
from .character_sheets import Outline, Reputation, Stats, HarmTrack, Character
from django.db import models


class DrivesSelect(models.Model)
    drive = models.ForeignKey(Drives)
    selectable = models.BooleanField(default=False)


class playbook(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    # Background
    drive1 = DrivesSelect


