from django.db import models
from .traits import *
from .playbook import *


# Characters need the following a:
# Character constants : name, species, details, demeanor, background 5 questions and 5 answers, 2 drives, 1 nature, 2 connections
# Character selections (these are traits that players have selected. I can't determine if you can later on add to your selection
# but best to leave those options open.): roguish_feats 9 options some pre chosen, weapon_skills 10 options, moves 6 options.
# Character varibles: reputation for each faction you have a reputation track which has 24 boxes, 5 stats -2 > +3, 3 harm tracks 4 boxes,
# equipment

class character(model.model):
    player = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    # background
    drive1 = models.ForeignKey(Drives, on_delete=models.CASCADE) # from traits selected by playbook
    drive2 = models.ForeignKey(Drives, on_delete=models.CASCADE) # from triats selected by playbook
    nature = models.ForeignKey(Natures, on_delete=models.CASCADE)
    connection1 = models.ForeignKey(Connections, on_delete=models.CASCADE)
    connection2 = models.ForeignKey(Connections, on_delete=models.CASCADE)



class char_name(models.Model):


class char_details(models.Model):


class char_demeanor(models.Model):
