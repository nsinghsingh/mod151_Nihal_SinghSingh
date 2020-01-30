from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from django.urls import reverse

# Create your views here.


def login(request, hasAccount=1):
    return render(request, 'login.html', {'hasAccount': hasAccount})


def register(request, hasAccount=0):
    return render(request, 'login.html', {'hasAccount': hasAccount})


def trylogin(request):
    login_name = request.POST['login_name']
    login_password = request.POST['login_password']
    try:
        user_data = User.objects.get(username=login_name)
    except(KeyError, User.DoesNotExist):
        return render(request, 'login.html', {
            'error_message': "Your password or username is incorrect",
            'hasAccount': 1,
            'login_name': login_name,
            'login_password': login_password
        })
    else:
        if user_data.password == login_password:
            request.session['IsLoggedIn'] = True
            request.session['username'] = login_name
            request.session.set_expiry(0)
            return HttpResponseRedirect(reverse('menu:browse'))
        else:
            return render(request, 'login.html', {
                'error_message': "Your password or username is incorrect",
                'hasAccount': 1,
                'login_name': login_name,
                'login_password': login_password
            })


def tryregister(request):
    login_name = request.POST['login_name']
    login_password = request.POST['login_password']
    try:
        user_data = User.objects.get(username=login_name)
    except(KeyError, User.DoesNotExist):
        if len(login_name) > 0 and len(login_password) > 0:
            new_entry = User(username=login_name, password=login_password)
            new_entry.save()
            return HttpResponseRedirect(reverse('login:login'))
        else:
            return render(request, 'login.html', {
                'error_message': "Please give in a username and password",
                'hasAccount': 0,
                'login_name': login_name,
                'login_password': login_password
            })
    else:
        return render(request, 'login.html', {
            'error_message': "That username already exists",
            'hasAccount': 0,
            'login_name': login_name,
            'login_password': login_password
        })


def logout(request):
    request.session.delete()
    return login(request, 1)
