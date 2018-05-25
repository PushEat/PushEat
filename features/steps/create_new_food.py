import time

from behave import *



use_step_matcher("parse")


@when("I search de navbar food button")
def step_impl(context):
    context.browser.find_by_id('btn-food').first.click()

@then("I create a food")
def step_impl(context):
    from food.models import Food
    context.browser.visit(context.get_url('users:add_food'))
    context.browser.find_by_id('new_food').first.click()
    dd = context.browser.find_by_tag('select')
    type = dd.find_by_tag('option').first.click()
    context.browser.fill('name', 'Tomato')
    context.browser.fill('calories', 52)
    context.browser.fill('fats', 70)
    context.browser.fill('protein', 20)
    form = context.browser.find_by_tag('form').first
    form.find_by_css('button.myButton').first.click()
    Food.objects.create(type= 'Main Dish', name='Tomato', calories=52, fats=70, protein=20)

@then("I create a food with his characteristics")
def step_impl(context):
    context.browser.visit(context.get_url('users:add_food'))
    header = context.browser.find_by_id('type')
    foodInfo = context.browser.find_by_id('foodInfo')
    for i, row in enumerate(context.table):
        assert row['type'] in header[i].text
        assert row['name'] in foodInfo[i].text
        assert row['calories'] in foodInfo[i].text
        assert row['fats'] in foodInfo[i].text
        assert row['proteins'] in foodInfo[i].text