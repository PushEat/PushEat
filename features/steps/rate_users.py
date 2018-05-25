from behave import *

use_step_matcher("re")


@then("I rate up a user")
def step_impl(context):
    context.browser.visit(context.get_url('/users/users_list'))