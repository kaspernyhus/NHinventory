from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from django.db.models.query import QuerySet
from django.forms import widgets
from .models import *


class CreateProjectForm(forms.ModelForm):
  class Meta:
    model = Project

    fields = (
      'name',
      'description',
    )