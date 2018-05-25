from behave import *

use_step_matcher("parse")


@then("I relocate my self at the main page")
def step_impl(context):
    header=context.browser.find_by_tag('h1')
    for i,row in enumerate(context.table):
        assert header == row['header']

@when("I want to see Home section")
def step_impl(context):
    context.browser.visit(context.get_url('home'))
    context.browser.find_by_id('home').first.click()