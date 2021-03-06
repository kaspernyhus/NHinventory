from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from django.db.models.query import QuerySet
from django.forms import widgets
from django.db.models import Q
from .models import *


class PartTypeFilterBox(forms.ModelForm):
  class Meta:
    model = Part

    fields = (
    'type',
    )
    
    labels = {
      'type': '',
    }

    widgets = {
      'type': forms.Select(attrs={'onchange': 'filterbox.submit();'}),
    }


class PartEditForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'


class PartCreateForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = '__all__'


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['stock','location']


class LocationUpdateForm(forms.ModelForm):
  class Meta:
        model = Location
        fields = ['container','placement']