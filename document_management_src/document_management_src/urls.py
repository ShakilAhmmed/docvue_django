"""document_management_src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles
from django.utils.translation import ugettext_lazy as _
from material.admin.sites import site

site.site_header = _('Document Management')
site.site_title = _('Document Management')
site.favicon = staticfiles('path/to/favicon')

urlpatterns = [
                  path('admin/', include('material.admin.urls')),
                  path('', include('login_panel.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
