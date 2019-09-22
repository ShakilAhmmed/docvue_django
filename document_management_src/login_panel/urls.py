from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_staff_admin, name="login"),
    path('admin_logout', views.logout_staff_admin, name="admin_logout"),
    path('backend', include('backend.urls')),
]
