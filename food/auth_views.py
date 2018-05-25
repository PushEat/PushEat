from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, render_to_response, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from models import *
from django.views.generic import ListView, CreateView
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
    return render_to_response('users/add_bids.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('users/invalid.html')


class AddAuctions(ListView):
    model = FoodOffer
    template_name = 'users/add_auctions.html'

    def get_context_data(self, **kwargs):
        context = super(AddAuctions, self).get_context_data(**kwargs)

        subscribeds = Subscribed.objects.all().filter(user=self.request.user)
        context['auctions'] = FoodOffer.objects.all().filter(owner=subscribeds)
        context['name'] = subscribeds.get()

        return context


class AddFoods(ListView):
    model = Food
    template_name = 'users/add_food.html'

    def get_context_data(self, **kwargs):
        context = super(AddFoods, self).get_context_data(**kwargs)

        context['name'] = Subscribed.objects.all().filter(user=self.request.user).get()
        context['foods'] = Food.objects.all()

        return context


def food_add_view(request):
    type = request.POST.get('type', '')
    name = request.POST.get('name', '')
    calories = request.POST.get('calories', '')
    fats = request.POST.get('fats', '')
    protein = request.POST.get('protein', '')

    food_obj = Food(type=type, name=name, calories=calories, fats=fats, protein=protein)
    food_obj.save()
    return HttpResponseRedirect(request.GET.get("next", "/users/add_food"))


class AddBids(ListView):
    model = Bid
    template_name = 'users/add_bids.html'

    def get_context_data(self, **kwargs):
        context = super(AddBids, self).get_context_data(**kwargs)
        subscribeds = Subscribed.objects.all().filter(user=self.request.user)
        context['bids'] = Bid.objects.all().filter(bidder=subscribeds)
        context['name'] = subscribeds.get()

        return context

class AuctionsUserView(ListView):
    model = FoodOffer
    template_name = 'users/user_last_auctions.html'

    def get_context_data(self, **kwargs):
        context = super(AuctionsUserView, self).get_context_data(**kwargs)

        context['auctions'] = FoodOffer.objects.all().order_by('-pk')
        return context

  
def auction_view(request, pk):
    if request.method == "GET":
        food = get_object_or_404(Food, pk=pk)

        member = get_member(request.user)

        dic = {
            "foods": Food.objects.all(),
            "food": food,
        }
        return render(request, 'users/new_auction.html', dic)
    else:
        user = Subscribed.objects.all().filter(user=request.user)

        food = get_object_or_404(Food, pk=pk)
        price = request.POST.get('price', '')
        desc = request.POST.get('desc', '')
        time = request.POST.get('time', '')

        # Generate foodOffer
        food_offer = FoodOffer(owner=user[0], food=food, start_price=price,
                               actual_price=price, description=desc, available_time=time)

        food_offer.save()

        return HttpResponseRedirect("/users/add_auctions")


def bids_view(request, pk):
    if request.method == "GET":
        food_offer = get_object_or_404(FoodOffer, pk=pk)

        member = get_member(request.user)

        dic = {
            "foodOffers": FoodOffer.objects.all(),
            "foodOffer": food_offer,
        }
        return render(request, 'users/new_bid.html', dic)
    else:
        user = Subscribed.objects.all().filter(user=request.user)

        food_offer = get_object_or_404(FoodOffer, pk=pk)
        price = request.POST.get('price', '')

        dic = {
            "foodOffers": FoodOffer.objects.all(),
            "foodOffer": food_offer,
            "error": "Bid amount must be bigger than actual auction price!"
        }

        if int(price) > food_offer.actual_price:
            # Generate Bid
            bid = Bid(bidder=user.get(), offer=food_offer, amount=price)
            food_offer.actual_price = price
            food_offer.save()
            bid.save()
        else:
            return render(request, 'users/new_bid.html', dic)

        return HttpResponseRedirect("/users/mybids")


def api_view(request):
    return render_to_response('users/api.html', {'full_name': request.user.username})


def del_auction(request, pk):

    auction = FoodOffer.objects.filter(pk=pk)
    auction.delete()

    return HttpResponseRedirect("/users/add_auctions")
