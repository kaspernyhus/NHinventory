from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from django.db.models.query import QuerySet
from django.forms import widgets
from django.db.models import Q
from .models import *
from bootstrap_modal_forms.forms import BSModalModelForm


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
        fields = (
          'name',
          'unit',
          'type',
          'subtype',
          'description',
          'footprint',
          'package',
          'stock',
          'datasheet',
          'url',
          'photo_thumbnail',
          'part_of_project'
          )


class PartCreateForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = (
          'name',
          'unit',
          'type',
          'subtype',
          'description',
          'footprint',
          'package',
          'stock',
          'datasheet',
          'url',
          'photo_thumbnail',
          'part_of_project'
          )


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['stock']