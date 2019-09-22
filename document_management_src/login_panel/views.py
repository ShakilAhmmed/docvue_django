from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .decorators import is_logged_in

from .forms import AdminLoginForm


# Create your views here.
@is_logged_in
def login_staff_admin(request):
    if request.method == "POST":
        form = AdminLoginForm(request.POST, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            logged_in_user = authenticate(request, username=username, password=password)
            if logged_in_user is not None:
                login(request, logged_in_user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = AdminLoginForm()
    context = {
        'form': form
    }
    return render(request, 'login_panel/index.html', context)


@login_required
def logout_staff_admin(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
