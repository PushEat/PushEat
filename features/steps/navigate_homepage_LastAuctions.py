import time

from behave import *

use_step_matcher("re")


@when("I want see LastAuctions section")
def step_impl(context):
    context.browser.visit(context.get_url('home'))
    context.browser.find_by_id('nonregLAuctions').first.click()


@then("I can see at least 1 auction")
def step_impl(context):
    context.browser.visit(context.get_url('last_auctions'))
    profiles = context.browser.find_by_css('.Auction')

    for i, row in enumerate(context.table):
        assert row['start_price'] in profiles[i].text
        assert row['actual_price'] in profiles[i].text
