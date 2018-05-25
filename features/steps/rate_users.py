from behave import *

use_step_matcher("re")


@then("I rate up a user")
def step_impl(context):
    context.browser.visit(context.get_url('/users/users_list'))
    value=context.browser.find_by_id('value')
    context.browser.find_by_id('btnStar').first.click()
    for i, row in enumerate(context.table):
        assert row['rate'] != value[i].text