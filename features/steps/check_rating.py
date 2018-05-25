
import time

from behave import *

use_step_matcher("parse")


@when("I check about my info")
def step_impl(context):
    about = context.browser.find_by_id('my-rate')
    about.find_by_css('a.w3-button').first.click()

@then("I will see my rate")
def step_impl(context):
    profiles = context.browser.find_by_id('my-stars')

    for i, row in enumerate(context.table):
        assert row['rate']  in profiles[i].text