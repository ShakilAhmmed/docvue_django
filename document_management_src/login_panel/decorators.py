from django.http import HttpResponseRedirect
from django.urls import reverse


def is_logged_in(view_function):
    def is_logged_in_check(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        else:
            return view_function(request, *args, **kwargs)

    return is_logged_in_check


def is_super_admin(view_function):
    def is_super_admin_check(request, *args, **kwargs):
        if request.user.is_superuser:
            return HttpResponseRedirect('/admin')
        else:
            return view_function(request, *args, **kwargs)

    return is_super_admin_check
