from django.conf.urls import url
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
    url(r'^add_bids/(?P<pk>\d+)$', CreateBid.as_view(), name='add_bid'),
    url(r'^mybids/$', AddBids.as_view(), name='show_bids'),
    url(r'^user_auctions', AuctionsUserView.as_view(), name='user_lastAuctions'),
    url(r'^new_auction/$', auction_view, name='auction_view'),

]
