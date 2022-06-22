from django.db import models
from .traits import *

# really need to think about whether these belong here
class Outline(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    details = models.CharField(max_length=180)
    demeanor = models.CharField(max_length=100)

class Stats(models.Model):
    charm = models.SmallIntegerField()
    cunning = models.SmallIntegerField()
    finesse = models.SmallIntegerField()
    luck = models.SmallIntegerField()
    might = models.SmallIntegerField()
