from behave import *


use_step_matcher("parse")


@when("I check top profiles")
def step_impl(context):
    context.browser.visit(context.get_url('popular_users'))



@then("I will see all top profiles including")
def step_impl(context):

    profiles = context.browser.find_by_css('.user-name')

    for i, row in enumerate(context.table):
        assert row['first_name'] + ", " + row['last_name'] == profiles[i].text


@given('Exists a subscribed created by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    from food.models import Subscribed

    for i, row in enumerate(context.table):
        first_name = row['first_name']
        pc = row['postal_code']
        age = row['age']
        rate = row['rate']
        last_name = row['last_name']
        Subscribed.objects.create(first_name=first_name, last_name=last_name, age=age, postal_code=pc,
                                  user=User.objects.get(username=username), rate=rate)