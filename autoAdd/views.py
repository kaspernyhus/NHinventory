from django.shortcuts import render, redirect
from inventory.models import *
import csv

def index(request):
  return render(request, 'autoAddIndex.html')


def run_auto_add(request):
  print("------------ reading .txt ------------")
  # try:
  with open('autoAdd/parts_to_import.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader) # skip first line
    for row in csv_reader:
      unit_type = None
      subtype = None
      location = None

      part_type = PartType.objects.get(pk=int(row[3]))
      if(row[2] != ''):
        unit_type = Unit.objects.get(pk=int(row[2]))
      if(row[4] != ''):
        subtype = Subtype.objects.get(pk=int(row[4]))
      if(row[9] != ''):
        location = Location.objects.get(pk=int(row[9]))

      newpart = Part(
        name=row[0],
        value=float(row[1]),
        unit = unit_type,
        type=part_type,
        subtype=subtype,
        description=row[5],
        footprint=row[6],
        package=row[7],
        stock=int(row[8]),
        location=location
        )
      newpart.save()

  # except:
  #   print("import file error")
  
  

  print("------------------------------------")
  return redirect('/')