from django.shortcuts import render, redirect
from .models import *
from BOMmanager.models import ProjectBOM
from .forms import *
from django.db.models import Q


def index(request):
  if request.GET.get('type'):
    filter_by = request.GET.get('type')
    parts_query = Part.objects.filter(type_id=filter_by).order_by('subtype','unit','value','name')
    form = PartTypeFilterBox(initial={'type': filter_by})
  
  elif request.GET.get('search_box'):
    search_query = request.GET.get('search_box')
    search_quaries = search_query.split()
    parts_query = Part.objects.all()
    form = PartTypeFilterBox(initial={'type': search_query})
  
  elif request.GET.get('stock'):
    new_stock = request.GET.get('stock')
    part_id = request.GET.get('part_id')
    part = Part.objects.get(pk=part_id)
    part.stock = new_stock
    part.updated = timezone.now()
    part.save()

    parts_query = Part.objects.all()
    form = PartTypeFilterBox()

  else:
    parts_query = Part.objects.order_by('type','subtype','unit','value','name')
    form = PartTypeFilterBox()

  context = {'parts': parts_query, 'form': form, 'stock_update_form': None}
  return render(request, 'index.html', context)


def create_part(request):
  if request.method == 'POST':
    form = PartCreateForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    return redirect('/')

  form = PartCreateForm()
  context = {'form': form}
  return render(request, 'create_part.html', context)


def edit_part(request, part_id):
  if request.method == 'POST':
    print('---------')
    print(request.FILES)
    form = PartEditForm(request.POST, request.FILES)
    if form.is_valid():
      form_tosave = form.save(commit=False)
      form_tosave.id = part_id
      form_tosave.save()
      return redirect('/')
  
  part = Part.objects.get(pk=part_id)
  form = PartEditForm(initial={
    'name':part.name,
    'value':part.value,
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
    'location':part.location
    })
  BOM = ProjectBOM.objects.filter(part=part)

  context = {'form': form, 'part': part, 'BOM':BOM}
  return render(request, 'edit_part.html', context)


def delete_part(request, part_id):
  part = Part.objects.get(pk=part_id)
  part.delete()
  return redirect('/')