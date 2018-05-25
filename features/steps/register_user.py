from behave import *

use_step_matcher("re")

@when("Register user")
def step_impl(context):
    from django.contrib.auth.models import User
    from food.models import Subscribed

    context.browser.visit(context.get_url('/users/register'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', 'user7')
    context.browser.fill('password1', '123password')
    context.browser.fill('password2', '123password')
    context.browser.fill('first_name', 'Antonieta')
    context.browser.fill('last_name', 'Palotes')
    context.browser.fill('age', '25')
    context.browser.fill('email', 'example@gmail.com')
    context.browser.fill('postal_code', '43001')
    form.find_by_css('button.w3-button').first.click()


@then('I login as user "user7" with password "123password"')
def step_impl(context):
    context.browser.visit(context.get_url('/users/login'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', 'user7')
    context.browser.fill('password', '123password')
    form.find_by_css('button.w3-button').first.click()
    assert context.browser.is_text_present('user7')
