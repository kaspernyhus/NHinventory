from django.contrib import admin
from .models import *


class PartAdmin(admin.ModelAdmin):
  list_display = ('name', 'description', 'value', 'unit', 'type', 'subtype', 'stock')


class LocationAdmin(admin.ModelAdmin):
  list_display = ('container', 'placement')

admin.site.register(Part, PartAdmin)
admin.site.register(PartType)
admin.site.register(Subtype)
admin.site.register(Unit)
admin.site.register(Location, LocationAdmin)
admin.site.register(Placement)