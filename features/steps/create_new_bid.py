import time

from behave import *

use_step_matcher("parse")

@step('Exists a foodOffer description "Uep, com anam"')
def step_impl(context):
    from food.models import FoodOffer, Food, Subscribed
    from django.contrib.auth.models import User
    FoodOffer.objects.create(owner=(Subscribed.objects.create(first_name='Josep', last_name='Figura', age=50,
                                                              postal_code=26000, user=User.objects.create(
                                                              username='user4', email='example@gmail.com',
                                                              password='123password'), rate=20)),
                            food=(Food.objects.create(type='Main Dish', name='Banana', calories=52, fats=70, protein=20)),
                             start_price=20, actual_price=20, description='Uep, com anam', available_time='11'+':' +'11')


@when("I want to create a new bid")
def step_impl(context):
    from food.models import Bid,Food,FoodOffer,Subscribed
    from django.contrib.auth.models import User
    context.browser.find_by_id('auctions').first.click()
    context.browser.find_by_id('newBid').first.click()
    context.browser.fill('price', 200)
    form = context.browser.find_by_tag('form').first
    form.find_by_css('button.myButton').first.click()
    sub=Subscribed.objects.create(first_name='Pepito', last_name='Figura', age=50,
                                                              postal_code=26000, user=User.objects.create(
                                                              username='user5', email='example@gmail.com',
                                                              password='123password'))

    offer = FoodOffer.objects.create(owner=(Subscribed.objects.create(first_name='Josefa', last_name='Figura', age=50,
                                                              postal_code=26000, user=User.objects.create(
                                                              username='user6', email='example@gmail.com',
                                                              password='123password'), rate=20)),
                            food=(Food.objects.create(type='Main Dish', name='Potato', calories=52, fats=70, protein=20)),
                             start_price=20, actual_price=20, description='Uep, com anam', available_time='11'+':' +'11')

    Bid.objects.create(bidder=sub, offer=offer, amount=200)



@then("I can see own bids")
def step_impl(context):
    bidInfo = context.browser.find_by_id('bidInfo')
    for i, row in enumerate(context.table):
        assert row['bidder'] in bidInfo[i].text
        assert row['offer'] in bidInfo[i].text
        assert row['amount'] in bidInfo[i].text
