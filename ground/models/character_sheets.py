from django.db import models
#from .traits import *
#from .playbook import *


# Characters need the following a:
# Character constants : name, species, details, demeanor, background 5 questions and 5 answers, 2 drives, 1 nature, 2 connections
# Character selections (these are traits that players have selected. I can't determine if you can later on add to your selection
# but best to leave those options open.): roguish_feats 9 options some pre chosen, weapon_skills 10 options, moves 6 options.
# Character varibles: reputation for each faction you have a reputation track which has 24 boxes, 5 stats -2 > +3, 3 harm tracks 4 boxes,
# equipment

class Outline(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    details = models.CharField(max_length=180)
    demeanor = models.CharField(max_length=100)


class Reputation(models.Model):
    faction = models.CharField(max_length=20)
    rep_number = models.PositiveSmallIntegerField(default=10)# 0-24

    @property
    def convert_rep_number(self):
        rep_structure = ["-3", "2.2", "2.1", "2", "1.2", "1.1", "1", ".2", ".1", "0", ".1", ".2", ".3", ".4", "1", "1.1", "1.2", "1.3", "1.4", "2", "2.1", "2.2", "2.3", "2.4", "3"]
        reputation = rep_structure[self.rep_number]
        return reputation


class Stats(models.Model):
    charm = models.SmallIntegerField()
    cunning = models.SmallIntegerField()
    finesse = models.SmallIntegerField()
    luck = models.SmallIntegerField()
    might = models.SmallIntegerField()


class HarmTrack(models.Model):
    injury = models.PositiveSmallIntegerField(default=0)
    exhaustion = models.PositiveSmallIntegerField(default=0)
    depletion = models.PositiveSmallIntegerField(default=0)


class Character(models.Model):
    player = models.CharField(max_length=20)
    outline = models.ForeignKey(Outline, on_delete=models.CASCADE)
    # need to get background from playbook
    drive1 = models.ForeignKey(Drives, on_delete=models.CASCADE) # from traits selected by playbook
    drive2 = models.ForeignKey(Drives, on_delete=models.CASCADE) # from traits selected by playbook
    nature = models.ForeignKey(Natures, on_delete=models.CASCADE) # from traits selected by playbook
    connection1 = models.ForeignKey(Connections, on_delete=models.CASCADE) # from traits selected by playbook
    connection2 = models.ForeignKey(Connections, on_delete=models.CASCADE) # from traits selected by playbook
