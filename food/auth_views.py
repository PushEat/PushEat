from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from models import Subscribed
from os import system
from views import get_member
import string
import random
import urlparse


def staff_login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('users/users_login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/users/loggedin')
    else:
        return HttpResponseRedirect('/users/invalid')


def loggedin(request):
    return render_to_response('users/loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('users/invalid.html')


def logout(request):
    auth.logout(request)
    return render_to_response('users/users_login.html')
