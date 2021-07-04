from django.contrib import admin

from .models import *


class ProjectAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectBOM)
