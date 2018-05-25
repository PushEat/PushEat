from behave import *

use_step_matcher("parse")


@when("I want to delete an auction I click the delete button")
def step_impl(context):
    from food.models import FoodOffer,Subscribed
    from django.contrib.auth.models import User

    context.browser.visit(context.get_url('/users/add_auctions'))
    context.browser.visit(context.get_url('users:add_food'))
    context.browser.find_by_id('createAuction').first.click()
    context.browser.fill('price', 20)
    context.browser.fill('desc', 'Uep, com anam')
    context.browser.fill('time', '11' + ':' + '11')
    form = context.browser.find_by_tag('form').first
    form.find_by_css('button.myButton').first.click()

    context.browser.find_by_id('del').first.click()





