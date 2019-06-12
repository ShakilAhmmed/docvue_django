from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from .forms import MyProjectsForm
from .models import MyProjectsModel


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
