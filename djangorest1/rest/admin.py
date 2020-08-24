from django.contrib import admin
from .models import Element, Reference

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'short_name', 'description', 'version', 'date')

class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'code', 'value')
# Register your models here.

admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Element, ElementAdmin)

