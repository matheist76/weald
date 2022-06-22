from django.db import models

# Create your models here.
# Character trait models here
# for Moves that is going to be difficult. Use a html special html form. So just a link. If there is a link then
# inherit or link it.
# Copy below for import list
# Outline, Background, Drives, Natures, Connections, WeaponSkills, RoguishFeats, Moves


class Background(models.Model):
    home = models.CharField(max_length=100)
    why = models.CharField(max_length=100)
    what = models.CharField(max_length=100)
    posifaction = models.CharField(max_length=100)
    negafaction = models.CharField(max_length=100)


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
    name = models.CharField(max_length=20, primary_key=True)


class WeaponSkills(models.Model):
    name = models.CharField(max_length=20, primary_key=True)


class Moves(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=300)
