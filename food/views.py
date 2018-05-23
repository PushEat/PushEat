# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from food.models import *
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


# Security Mixins
class LoginRequiredMixinStaff(object):
    @method_decorator(login_required(login_url='/user/profile'))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


def food_view(request):
    return render(request, 'food.html')


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
        context['users'] = Subscribed.objects.all().filter(user=self.request.user)

        return context


class UsersListView(ListView):
    model = Subscribed
    template_name = 'users_list.html'

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['usersList'] = Subscribed.objects.all().order_by('-rate')
        return context


@login_required(login_url='/users/login')
def add_star(request, pk):
    subscribed_obj = Subscribed.objects.filter(pk=pk)
    user_obj = subscribed_obj.get().user

    subscribed_me = Subscribed.objects.filter(user=request.user)

    friendship = Friendship.objects.filter(me=subscribed_me[0])

    if not friendship:
        print "CASE: NO EXISTS"
        friendship = Friendship(id(subscribed_me),me=subscribed_me[0])
        friendship.save()
        rate = subscribed_obj.get().rate
        rate += 1
        Subscribed.objects.filter(pk=pk).update(rate=rate)
        friendship.friends.add(user_obj)

    elif friendship.get().friends.exists():
        print "CASE: FRIENDS EXIST"
        if friendship.get().friends.all().count() == 0:
            print "CASE: 0 FRIENDS"
            rate = subscribed_obj.get().rate
            rate += 1
            Subscribed.objects.filter(pk=pk).update(rate=rate)
            friendship.get().friends.add(user_obj)
        else:
            if user_obj not in friendship.get().friends.all():
                print "CASE: +1 FRIEND EXISTS + NO FOUND(add)"
                rate = subscribed_obj.get().rate
                rate+=1
                Subscribed.objects.filter(pk=pk).update(rate=rate)
                friendship.get().friends.add(user_obj)
            else:
                print "CASE: +1 FRIEND EXISTS + FOUND"
                rate = subscribed_obj.get().rate
                rate -= 1
                Subscribed.objects.filter(pk=pk).update(rate=rate)
                friendship.get().friends.remove(user_obj)
    else:
        print "CASE: FRIENDS NO EXISTS"
        if friendship.get().friends.all().count() == 0:
            print "CASE: 0 FRIENDS"
            rate = subscribed_obj.get().rate
            rate += 1
            Subscribed.objects.filter(pk=pk).update(rate=rate)
            friendship.get().friends.add(user_obj)
        else:
            if user_obj not in friendship.get().friends.all():
                print "CASE: +1 FRIEND EXISTS + NO FOUND (add)"
                rate = subscribed_obj.get().rate
                rate+=1
                Subscribed.objects.filter(pk=pk).update(rate=rate)
                friendship.friends.add(user_obj)
            else:
                print "CASE: +1 FRIEND EXISTS + FOUND"
                rate = subscribed_obj.get().rate
                rate -= 1
                Subscribed.objects.filter(pk=pk).update(rate=rate)
                friendship.get().friends.remove(user_obj)

    return HttpResponseRedirect("/users/users_list")

