from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q


def index(request):
  print(request.GET)
  if request.GET.get('type'):
    filter_by = request.GET.get('type')
    print(filter_by)
    parts_query = Part.objects.filter(type_id=filter_by)
    form = PartTypeFilterBox(initial={'type': filter_by})
  
  elif request.GET.get('search_box'):
    search_query = request.GET.get('search_box')
    search_quaries = search_query.split()
    print(search_quaries)
    parts_query = Part.objects.all()
    form = PartTypeFilterBox(initial={'type': search_query})
  
  else:
    parts_query = Part.objects.all()
    form = PartTypeFilterBox()

  context = {'parts': parts_query, 'form': form}
  return render(request, 'index.html', context)


def edit_part(request, part_id):
  if request.method == 'POST':
    form = PartEditForm(request.POST)
    if form.is_valid():
      form_tosave = form.save(commit=False)
      form_tosave.id = part_id
      form_tosave.save()
      return redirect('/')
  
  part = Part.objects.get(pk=part_id)
  form = PartEditForm(initial={
    'name':part.name,
    'unit':part.unit,
    'type':part.type,
    'subtype':part.subtype,
    'description':part.description,
    'footprint':part.footprint,
    'package':part.package,
    'stock':part.stock,
    'datasheet':part.datasheet,
    'url':part.url,
    'photo_thumbnail':part.photo_thumbnail,
    'part_of_project':part.part_of_project
    })

  context = {'form': form}
  return render(request, 'edit_part.html', context)