# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from food.models import *
from django.views.generic import ListView

# Security Mixins
class LoginRequiredMixinStaff(object):
    @method_decorator(login_required(login_url='/user/profile'))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


def food_view(request):
    return render(request, 'pushEat/homepage.html')


def profile_view(request):
    return render(request, 'users/profile.html')


def login_page(request):
    return HttpResponseRedirect("/user/profile")

def popular_users(request):
    return render(request, 'popular_users.html')

def get_member(user):
    if Subscribed.objects.filter(user=user).exists():
        return Subscribed.objects.get(user=user)

    return None

class popularUsersView(ListView):
    model = Subscribed
    template_name = 'popular_users.html'
