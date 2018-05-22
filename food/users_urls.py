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
    url(r'^add_food/$', AddFoods.as_view(), name='add_food'),
    url(r'^new_auction/$', auction_view, name='auction_view'),
    url(r'^my_valoration/', MyValorationView.as_view(), name='my_valoration'),
    url(r'^users_list/', UsersListView.as_view(), name='users_list'),
]
