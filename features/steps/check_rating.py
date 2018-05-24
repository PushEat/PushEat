from behave import *

use_step_matcher("re")


@when("I check about my info")
def step_impl(context):
    context.browser.visit(context.get_url('users:my_valoration'))

@then("I will see my rate")
def step_impl(context):
    profiles = context.browser.find_by_css('.valoration')

    for i, row in enumerate(context.table):
        assert row['first_name'] + ", " + row['last_name'] + ", " + row['rate'] == profiles[i].text