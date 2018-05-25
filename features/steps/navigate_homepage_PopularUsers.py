from behave import *

use_step_matcher("parse")


@when("I want too see PopularUsers section")
def step_impl(context):
    context.browser.visit(context.get_url('home'))
    context.browser.find_by_id('nonregPUsers').first.click()


@then("I can see 1 top rated user")
def step_impl(context):

    profiles = context.browser.find_by_id('user-name')

    for i, row in enumerate(context.table):
        assert row['first_name'] + ", " + row['last_name'] == profiles[i].text