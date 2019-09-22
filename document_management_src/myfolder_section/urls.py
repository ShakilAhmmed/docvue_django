from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.my_projects, name="my_projects"),
    path('projects/edit/<int:pk>', views.my_projects_edit, name="my_projects_edit"),
    path('folder/<int:pk>', views.folder, name="folder"),
    path('my_file', views.my_file, name="my_file"),
]
