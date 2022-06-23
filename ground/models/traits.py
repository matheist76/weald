from django.db import models

# Create your models here.
# Character trait models here
# for Moves that is going to be difficult. Use a html special html form. So just a link. If there is a link then
# inherit or link it.
# Copy below for import list
# Background, Drives, Natures, Connections, WeaponSkills, RoguishFeats, Moves

class Options(models.Model):
    selectable = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=180)


class BgQuestions(models.Model):
    QUESTION_TYPES_CHOICES = (('Q1', 'Where'), ('Q2', 'Why'), ('Q3', 'Whom or What'), ('Q4', 'Amity Faction'), ('Q5', 'Enmity Faction'))
    question = models.CharField(max_length=100)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES_CHOICES)


class BgAnswers(models.Model):
    description = models.CharField(max_length=100)
    quest_id = models.ForeignKey(BgQuestions, on_delete=models.CASCADE)
    player_added_txt = models.CharField(max_length=20)
    selectable = models.BooleanField(default=False)


class Drives(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=180)


class Natures(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=180)


class Connections(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=300)
    sub_description = models.CharField(max_length=300)


class RoguishFeats(models.Model):
    name = models.CharField(max_length=20)
    selectable = models.BooleanField(default=False)
    bold = models.BooleanField(default=False)


class WeaponSkills(models.Model):
    name = models.CharField(max_length=20)
    selectable = models.BooleanField(default=False)
    bold = models.BooleanField(default=False)


class Ranges(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class WeaponSkillTag(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name

class SpecialTags(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=200)
    bullet_type = models.SmallIntegerField()

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=20)
    wear = models.PositiveSmallIntegerField()
    cost = models.PositiveSmallIntegerField()
    ranges = models.ManyToManyField(Ranges, related_name="equipments", blank=True)
    harm = models.CharField(max_length=20)
    weapon_skill_tags = models.ManyToManyField(WeaponSkillTag, related_name="equipments", blank=True)
    special_tags = models.ManyToManyField(SpecialTags, related_name="equipments", blank=True)


class Moves(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=300)
    options = models.ForeignKey(Options, on_delete=models.CASCADE, blank=True, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, blank=True, null=True)
