from behave import *
import sys
use_step_matcher("re")


@when("I create restaurant")
def step_impl(context):
    context.browser.visit(context.get_url('food:add_auction'))
    
