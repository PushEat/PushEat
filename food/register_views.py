from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class UserRegister(CreateView):
    model = User
    template_name = "templates/users/user_register.html"
    from_class = UserCreationForm
    success_url = reverse_lazy('templates/base/leftBar.html')
