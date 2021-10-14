from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('run', views.run_auto_add, name='run_auto_add'),
  ]