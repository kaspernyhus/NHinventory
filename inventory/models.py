from django.db import models
from django.utils import timezone


class PartTypes(models.Model):
  type = models.CharField(max_length=50)


class Projects(models.Model):
  name = models.CharField(max_length=100, blank=False)
  updated = models.DateTimeField(default=timezone.now)


class Part(models.Model):
  name = models.CharField(max_length=100, blank=False)
  type = models.ForeignKey(PartTypes, on_delete=models.CASCADE)
  description = models.CharField(max_length=200, blank=True, null=True)
  footprint = models.CharField(max_length=50, blank=True, null=True)
  package = models.CharField(max_length=50, blank=True, null=True)
  stock = models.IntegerField(default=0, blank=False)
  updated = models.DateTimeField(default=timezone.now)
  datasheet = models.URLField(max_length=200, blank=True, null=True)
  photo_thumbnail = models.ImageField(upload_to='photos/thumbnails/', blank=True)
  part_of_project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)