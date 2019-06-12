from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/my_folder/', include('myfolder_section.urls')),
]
