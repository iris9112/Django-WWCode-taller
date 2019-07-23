from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Service, Project

# Register your models here.

# admin.site.register(Service)
admin.site.register(Project)

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    pass