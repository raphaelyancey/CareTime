from django.contrib import admin
from .models import *


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'parent_organization',)}


class HostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('last_name',)}


# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Appointment)
