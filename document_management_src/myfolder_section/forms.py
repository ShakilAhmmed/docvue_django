from django import forms

from .models import MyProjectsModel, Folder


class MyProjectsForm(forms.ModelForm):
    class Meta:
        model = MyProjectsModel
        fields = "__all__"
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 5}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = "__all__"
        widgets = {
            'folder_name': forms.TextInput(attrs={'class': 'form-control'}),
            'folder_description': forms.Textarea(attrs={'class': 'form-control'}),
            'parent_folder': forms.HiddenInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),

        }
