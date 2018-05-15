# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
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

    def get_context_data(self, **kwargs):
        context = super(popularUsersView, self).get_context_data(**kwargs)
        context['popularusers'] = Subscribed.objects.all().order_by('-rate')[:4]
        return context

class AuctionsView(ListView):
    model = FoodOffer
    template_name = 'lastAuctions.html'

    def get_context_data(self, **kwargs):
        context = super(AuctionsView, self).get_context_data(**kwargs)

        context['auctions'] = FoodOffer.objects.all().order_by('-pk')
        return context


class MyValorationView(ListView):
    model = Subscribed
    template_name = 'my_valoration.html'

    def get_context_data(self, **kwargs):
        context = super(MyValorationView, self).get_context_data(**kwargs)
        context['myvaloration'] = Subscribed.objects.all().order_by('-rate')[:1]
        return context