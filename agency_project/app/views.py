from django.views.generic.list import ListView

from app.models import Service, Project


class ServiceListView(ListView):
    model = Service
    template_name = 'app/list_services.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'app/list_projects.html'
