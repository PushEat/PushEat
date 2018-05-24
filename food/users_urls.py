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
    url(r'^add_bids/(?P<pk>\d+)$', add_bids, name='add_bid'),
    url(r'^mybids/$', AddBids.as_view(), name='show_bids'),
    url(r'^user_auctions', AuctionsUserView.as_view(), name='user_lastAuctions'),
    url(r'^del_auction/(?P<pk>\d+)', del_auction, name='add_auctions'),
    url(r'^add_food/$', AddFoods.as_view(), name='add_food'),
    url(r'^my_valoration/', MyValorationView.as_view(), name='my_valoration'),
    url(r'^users_list/', UsersListView.as_view(), name='users_list'),
    url(r'^add_star/(?P<pk>\d+)', add_star, name='add_star'),
    url(r'^new_auction/(?P<pk>\d+)', auction_view, name='auction_view'),
    url(r'^new_food/$', food_add_view, name='food_view'),
    url(r'^api/$', api_view, name='food_view'),
]
