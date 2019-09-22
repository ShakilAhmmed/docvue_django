from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from login_panel.decorators import is_super_admin


# Create your views here.


@login_required
@is_super_admin
def home(request):
    return render(request, 'admin_panel/home.html')
