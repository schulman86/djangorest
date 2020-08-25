from django.contrib import admin
from .models import Element, Reference

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'name', 'short_name', 'description', 'version', 'date')
    list_filter = ('name',)
    search_fields = ('name', 'short_name', 'uuid')
    date_hierarchy = 'date'

class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'code', 'value')
    list_filter = ('parent_id',)
    search_fields = ('parent_id', 'code', 'value')
    raw_id_fields = ('parent_id',)
# Register your models here.

admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Element, ElementAdmin)

