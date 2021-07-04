from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='BOMmanager_index'),
  path('BOM<int:project_id>', views.show_BOM, name='show_BOM'),
  path('create', views.create_project, name='create_project'),
  ]