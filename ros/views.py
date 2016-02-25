from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

def login(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    return render_to_response('login.html', csrf_dict)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        if request.POST.has_key('next'):
            return HttpResponseRedirect(request.POST['next'])
        else:
            return HttpResponseRedirect('/ros/index/')
    else:
        return HttpResponseRedirect('/ros/invalid/')


def invalid_login(request):
        return HttpResponseRedirect('/ros/login')


@login_required(login_url='/ros/login/')
def index(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('index.html', {'username': request.user.username})
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)


@login_required(login_url='/ros/login/')
def products(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('products.html')
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)


@login_required(login_url='/ros/login/')
def customers(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('customers.html')
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)


@login_required(login_url='/ros/login/')
def transactions(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('transactions.html')
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)

def logout(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    auth.logout(request)
    return render_to_response('login.html', csrf_dict)
