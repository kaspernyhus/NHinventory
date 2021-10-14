from django.shortcuts import render, redirect
from .models import *
from .forms import *
from inventory.models import Part


def index(request):
  projects = Project.objects.all()

  context = {'projects': projects}
  return render(request, 'BOM_manager.html', context)


def show_BOM(request, project_id):
  if request.GET.get('stock'):
    new_stock = request.GET.get('stock')
    part_id = request.GET.get('part_id')
    part = Part.objects.get(pk=part_id)
    part.stock = new_stock
    part.save()
  if request.GET.get('qty'):
    new_qty = request.GET.get('qty')
    BOM_part_id = request.GET.get('part_id')
    part = ProjectBOM.objects.get(pk=BOM_part_id)
    part.qty = new_qty
    part.date = timezone.now()
    part.save()
  
  project = Project.objects.get(pk=project_id)
  parts = ProjectBOM.objects.filter(project=project).order_by('part__type')
  
  context = {'project': project, 'parts':parts}
  return render(request, 'BOM_list.html', context)


def create_project(request):
  if request.method == 'POST':
    form = CreateProjectForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('/projects')

  form = CreateProjectForm()

  context = {'form': form}
  return render(request, 'create_project.html', context)


def BOM_add_part(request, project_id):
  #print(request.GET, request.POST)
  
  project = Project.objects.get(pk=project_id)

  if request.POST.getlist('add_part'):
    part_id_POST = request.POST.getlist('part')
    part_id_name = part_id_POST[0].split(':') # seperate by ':'
    
    # if 'id:' present
    if len(part_id_name) == 2:
        part_id = part_id_name[0]
        part_name = part_id_name[1].strip()
    # if not propably a user input = new ingredient
    else:
        part_id = 0
        part_name = part_id_name[0]
    # Try to get object from db
    try:
        part_query = Part.objects.get(pk=part_id)
    # if not found in data base create new ingredient
    except:
      next_path = request.path
      return redirect('/create?next='+next_path+'&part_name='+part_name)
    part_quantity = request.POST.getlist('qty')
    part_refs = request.POST.get('pcb_ref')
    part_to_add = ProjectBOM(project=project, part=part_query, qty=part_quantity[0], pcb_ref=part_refs, date=timezone.now())
    part_to_add.save()
  
  if request.GET.get('qty'):
    new_qty = request.GET.get('qty')
    BOM_part_id = request.GET.get('part_id')
    part = ProjectBOM.objects.get(pk=BOM_part_id)
    part.qty = new_qty
    part.date = timezone.now()
    part.save()
    


  parts = Part.objects.all()
  BOM_parts = ProjectBOM.objects.filter(project=project_id)
  context = {'project': project, 'parts': parts, 'BOM_parts': BOM_parts}
  return render(request, 'BOM_add_part.html', context)


def BOM_delete_part(request, project_id, part_id):
  part = ProjectBOM.objects.get(pk=part_id)
  part.delete()
  return redirect('/projects/BOM' + str(project_id))


def export_missing(request, project_id):
  project = Project.objects.get(pk=project_id)
  parts = Part.objects.all()
  BOM_parts = ProjectBOM.objects.filter(project=project_id)


  context = {'project': project, 'parts': parts, 'BOM_parts': BOM_parts}
  return render(request, 'BOM_missing_list.html', context)