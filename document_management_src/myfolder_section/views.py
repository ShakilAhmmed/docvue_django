from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from .forms import MyProjectsForm, FolderForm, FileForm
from .models import MyProjectsModel, Folder, FileModel


# Create your views here.
def my_projects(request):
    projects_data = MyProjectsModel.objects.filter(is_deleted=False).order_by('-id')

    # Form Data Save and Error Message Show,,, First Check POST THEN GET THEN DELETE
    if request.method == 'POST':
        form = MyProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Project Created Successfully')
            return HttpResponseRedirect(reverse('my_projects'))
    else:
        form = MyProjectsForm()

    if request.method == "POST" and request.POST.get('_method') == "DELETE":
        project_id = request.POST.get('delete_pk')
        project_delete = get_object_or_404(MyProjectsModel, pk=project_id)
        project_delete.soft_delete()
        messages.warning(request, 'Project Moved Into Trash')
        return HttpResponseRedirect(reverse('my_projects'))

    context = {
        'form': form,
        'projects_data': projects_data
    }
    return render(request, 'admin_panel/my_folder_section/my_projects/my_projects_entry_form.html', context)


def my_projects_edit(request, pk):
    project_edit = get_object_or_404(MyProjectsModel, pk=pk)
    if request.method == "POST":
        form = MyProjectsForm(request.POST, instance=project_edit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Updated Successfully')
            return HttpResponseRedirect(reverse('my_projects_edit', kwargs={'pk': pk}))
    form = MyProjectsForm(instance=project_edit)
    context = {
        'form': form
    }

    return render(request, 'admin_panel/my_folder_section/my_projects/my_projects_edit_form.html', context)


def folder(request, pk=0):
    folder_data = Folder.objects.filter(parent_folder=pk)
    files = FileModel.objects.filter(parent_folder=pk)
    file_form = FileForm()
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Folder Created Successfully')
            return HttpResponseRedirect(reverse('folder', kwargs={'pk': pk}))
    else:
        form = FolderForm()
    context = {
        'form': form,
        'file_form': file_form,
        'parent_folder': pk,
        'folder_data': folder_data,
        'files': files
    }
    return render(request, 'admin_panel/my_folder_section/folder/folder.html', context)


def my_file(request):
    #
    if request.method == "POST":
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_save = file_form.save(commit=False)
            folder_data = request.POST.get('parent_folder')
            file_save.parent_folder = folder_data
            file_save.save()
            messages.success(request, 'File Added Successfully')
        return HttpResponseRedirect(reverse('folder', kwargs={'pk': request.POST.get('parent_folder')}))
