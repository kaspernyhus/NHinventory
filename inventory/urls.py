from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('edit<int:part_id>', views.edit_part, name='edit_part'),
  path('create', views.create_part, name='create_part'),
  path('delete<int:part_id>', views.delete_part, name='delete_part'),
  ]