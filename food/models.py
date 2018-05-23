# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
# from django_countries.fields import CountryField
from django.db import models
from datetime import date


class Subscribed(models.Model):
    subscribed_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(blank=False, max_length=16)
    last_name = models.CharField(blank=False, max_length=16)
    age = models.PositiveIntegerField(blank=False)
    address = models.CharField(blank=False, max_length=64)
    # country = CountryField()
    postal_code = models.PositiveIntegerField()
    subscription_date = models.DateField(default=date.today)
    rate = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return u"%s" % self.first_name

    def __unicode__(self):
        return u"%s" % self.first_name


class Friendship(models.Model):
    me = models.OneToOneField(Subscribed, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User)


class Food(models.Model):
    type = models.CharField(blank=False, max_length=32)
    name = models.CharField(blank=False, max_length=32)
    calories = models.PositiveIntegerField(blank=False)
    fats = models.PositiveIntegerField(blank=False)
    protein = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class FoodOffer(models.Model):
    owner = models.ForeignKey(Subscribed, related_name='created_by')
    purchaser = models.ForeignKey(Subscribed, blank=True, null=True, related_name='bidded_by')
    food = models.ForeignKey(Food, related_name='contains')

    start_price = models.PositiveIntegerField(blank=False, null=False)
    actual_price = models.PositiveIntegerField(blank=False, null=False)
    last_price = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(blank=False, max_length=64, null=False)
    available_time = models.TimeField(blank=False, null=False)

    def __str__(self):
        return u"%s" % self.owner.first_name + ", " + self.food.name

    def __unicode__(self):
        return u"%s" % self.owner.first_name + ", " + self.food.name


class Bid(models.Model):
    bidder = models.ForeignKey(Subscribed, related_name='made_by')
    offer = models.ForeignKey(FoodOffer, related_name='done_on')

    amount = models.PositiveIntegerField(blank=False)


class Message(models.Model):
    send_by = models.ForeignKey(Subscribed, related_name='send_by')
    send_to = models.ForeignKey(Subscribed, related_name='send_to')
    body = models.CharField(blank=False, max_length=512)
    date = models.DateTimeField(default=date.today)
