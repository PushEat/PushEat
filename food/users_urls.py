from django.conf.urls import url
from django.views.generic import TemplateView

from food.auth_views import *
from food.register_views import register
from views import *

urlpatterns = [
    url(r'^login/$', staff_login, name="login"),
    url(r'^auth/$', auth_view, name="auth_view"),
    url(r'^loggedin/$', loggedin, name="loggedin"),
    url(r'^invalid/$', invalid_login, name="invalid_login"),
    url(r'^register/', register, name="user_register"),
    url(r'^add_auctions/$', AddAuctions.as_view(), name='add_auctions'),
    url(r'^add_food/$', AddFoods.as_view(), name='add_food'),
    url(r'^new_auction/(?P<pk>\d+)', auction_view, name='auction_view'),
    url(r'^new_food/$', food_add_view, name='food_view'),
    url(r'^api/$', api_view, name='food_view'),
]
