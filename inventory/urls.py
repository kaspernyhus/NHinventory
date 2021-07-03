from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('edit<int:part_id>', views.edit_part, name='edit_part')
  ]