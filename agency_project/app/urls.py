from django.urls import path
from app.views import ServiceListView, ProjectListView

app_name = "app"

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]