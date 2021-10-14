from django.urls import path
from . import views

urlpatterns = [
  path('', views.autoadd_index, name='autoadd_index'),
  path('run', views.run_auto_add, name='run_auto_add'),
  ]