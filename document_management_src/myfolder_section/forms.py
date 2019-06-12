from django import forms

from .models import MyProjectsModel


class MyProjectsForm(forms.ModelForm):
    class Meta:
        model = MyProjectsModel
        fields = "__all__"
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 5}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
        }
