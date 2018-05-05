# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.


def food_view(request):
    return render(request, 'pushEat/homepage.html')


def profile_view(request):
    return render(request, 'users/profile.html')