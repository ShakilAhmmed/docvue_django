from material.admin.decorators import register
from material.admin.options import MaterialModelAdmin
from .models import MyProjectsModel


# Register your models here.

@register(MyProjectsModel)
class Project(MaterialModelAdmin):
    icon_name = 'project'
    list_display = ['project_name', 'project_description', 'created_by']
    list_per_page = 5
