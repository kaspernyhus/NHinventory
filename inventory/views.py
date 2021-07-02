from django.shortcuts import render
from .models import *

def index(request):
  all_parts = Part.objects.all()

  return render(request, 'index.html', {'all_parts': all_parts})