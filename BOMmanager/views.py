from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
  projects = Project.objects.all()

  context = {'projects': projects}
  return render(request, 'BOM_manager.html', context)


def show_BOM(request, project_id):
  project = Project.objects.get(pk=project_id)
  parts = ProjectBOM.objects.filter(project=project).order_by('part__type')
  print('----------')
  print(parts)
  
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