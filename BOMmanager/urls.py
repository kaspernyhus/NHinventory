from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='BOMmanager_index'),
  path('BOM<int:project_id>', views.show_BOM, name='show_BOM'),
  path('create', views.create_project, name='create_project'),
  path('add_part/<int:project_id>', views.BOM_add_part, name='BOM_add_part'),
  path('delete_part/<int:project_id>/<int:part_id>', views.BOM_delete_part, name='BOM_delete_part'),
  path('BOMmissing<int:project_id>', views.export_missing, name='export_missing_BOM'),
  ]