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
]
