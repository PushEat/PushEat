from django.conf.urls import url
from food.auth_views import *
from food.register_views import UserRegister
from views import *

urlpatterns = [
    url(r'^login/$', staff_login, name="login"),
    url(r'^auth/$', auth_view, name="auth_view"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^loggedin/$', loggedin, name="loggedin"),
    url(r'^invalid/$', invalid_login, name="invalid_login"),
    url(r'^register/$', UserRegister.as_view(), name="user_register"),
]
