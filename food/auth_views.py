

from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from models import *
from django.views.generic import ListView
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


class AddAuctions(ListView):
    model = FoodOffer
    template_name = 'users/add_auctions.html'

    def get_context_data(self, **kwargs):
        context = super(AddAuctions, self).get_context_data(**kwargs)

        print "BEFORE"
        subscribeds = Subscribed.objects.all().filter(user=self.request.user)
        context['auctions'] = FoodOffer.objects.all().filter(owner=subscribeds)
        context['name'] = subscribeds.get()

        return context


def auction_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # new instance of FoodOffer

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/users/loggedin')
    else:
        return HttpResponseRedirect('/users/invalid')

# Si no tenen el mateix nom (User-Subscribbed) peta
# user = Subscribed.objects.all().filter(user=self.request.user)
# users = Subscribed.objects.all()


class AddBids(ListView):
    model = Bid
    template_name = 'users/add_bids.html'

    def get_context_data(self, **kwargs):
        context = super(AddBids, self).get_context_data(**kwargs)

        subscribeds = Subscribed.objects.all().filter(user=self.request.user)
        context['bids'] = Bid.objects.all().filter(bidder=subscribeds)
        context['name'] = subscribeds.get()
        context['foods'] = FoodOffer.objects.all()

        return context

def bid_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # new instance of Bid

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/users/add_bids')
    else:
        return HttpResponseRedirect('/users/invalid')
