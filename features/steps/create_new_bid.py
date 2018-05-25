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
    """
    :type context: behave.runner.Context
    """
    pass


@then("I can see own bids")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass