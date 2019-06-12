from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.my_projects, name="my_projects"),
    path('projects/edit/<int:pk>', views.my_projects_edit, name="my_projects_edit")
]
