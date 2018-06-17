from django.contrib import admin

# Register your models here.
from app.sites.models import Sites, Value


class SitesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ValueAdmin(admin.ModelAdmin):
    list_display = ('site', 'date', 'a_value', 'b_value')
    search_fields = ('date',)

admin.site.register(Sites, SitesAdmin)
admin.site.register(Value, ValueAdmin)