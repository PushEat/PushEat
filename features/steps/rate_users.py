from behave import *
import time
use_step_matcher("re")


@then("I rate up a user")
def step_impl(context):
    context.browser.visit(context.get_url('/users/users_list'))
    context.browser.find_by_id('btnStar').first.click()
    star = context.browser.find_by_id('value')

    for i,row in enumerate(context.table):
        assert row['rate'] in star[i].text