from django.db import models

# Create your models here.
from django.utils import timezone

from .validators import clean_project_name


class MyProjectsModel(models.Model):
    project_name = models.CharField(max_length=150, unique=True, validators=[clean_project_name])
    project_description = models.TextField()
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        print("ok")
        self.save()

    class Meta:
        db_table = "my_projects"
