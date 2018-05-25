from behave import *



use_step_matcher("parse")


@given('Exists a food name "Banana"')
def step_impl(context):
    from food.models import Food
    Food.objects.create(type='Main Dish', name='Banana', calories=52, fats=70, protein=20)

@when("I create a new auction")
def step_impl(context):
    from food.models import FoodOffer,Food, Subscribed
    from django.contrib.auth.models import User
    context.browser.visit(context.get_url('users:add_food'))
    context.browser.find_by_id('createAuction').first.click()
    context.browser.fill('price', 20)
    context.browser.fill('desc', 'Uep, com anam')
    context.browser.fill('time', '11'+':' +'11')
    form = context.browser.find_by_tag('form').first
    form.find_by_css('button.myButton').first.click()
    FoodOffer.objects.create(owner=(Subscribed.objects.create(first_name='Josep', last_name='Figura', age=50,
                                                              postal_code=26000, user=User.objects.create(
                                                              username='user4', email='example@gmail.com',
                                                              password='123password'), rate=20)),
                            food=(Food.objects.create(type='Main Dish', name='Banana', calories=52, fats=70, protein=20)),
                             start_price=20, actual_price=20, description='Uep, com anam', available_time='11'+':' +'11')


@then("I'm viewing the details of the auction")
def step_impl(context):
    context.browser.visit(context.get_url('users:add_auctions'))
    auctionInfo = context.browser.find_by_id('auctionInfo')
    for i, row in enumerate(context.table):
        assert row['start_price'] in auctionInfo[i].text
        assert row['actual_price'] in auctionInfo[i].text
        assert row['description'] in auctionInfo[i].text
        assert row['available_time'] in auctionInfo[i].text