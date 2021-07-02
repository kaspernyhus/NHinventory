from django.db import models
from django.utils import timezone


class PartType(models.Model):
  type = models.CharField(max_length=50)
  
  def __str__(self):
    return self.type


class Subtype(models.Model):
  subtype = models.CharField(max_length=50)

  def __str__(self):
    return self.subtype


class Unit(models.Model):
  unit = models.CharField(max_length=20, blank=False)

  def __str__(self):
    return self.unit


class Project(models.Model):
  name = models.CharField(max_length=100, blank=False)
  updated = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name


class Part(models.Model):
  name = models.CharField(max_length=100, blank=False)
  value = models.FloatField(blank=True, null=True)
  unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, blank=True, null=True)
  type = models.ForeignKey(PartType, on_delete=models.DO_NOTHING)
  subtype = models.ForeignKey(Subtype, on_delete=models.DO_NOTHING, blank=True, null=True)
  description = models.CharField(max_length=200, blank=True, null=True)
  footprint = models.CharField(max_length=50, blank=True, null=True)
  package = models.CharField(max_length=50, blank=True, null=True)
  stock = models.IntegerField(default=0, blank=False)
  updated = models.DateTimeField(default=timezone.now)
  datasheet = models.URLField(max_length=200, blank=True, null=True)
  photo_thumbnail = models.ImageField(upload_to='photos/thumbnails/', blank=True, null=True)
  part_of_project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=True, null=True)

  def __str__(self):
    return self.name