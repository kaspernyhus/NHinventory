from django.db import models
from django.utils import timezone
from inventory.models import Part


class Project(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=300, blank=True)
  date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name


class ProjectBOM(models.Model):
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  part = models.ForeignKey(Part, on_delete=models.DO_NOTHING)
  qty = models.IntegerField(default=1, blank=False)
  date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.part.name