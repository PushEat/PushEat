from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from food.models import Bid


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    age = forms.IntegerField(max_value=150, required=True, help_text='Enter your age please')
    postal_code = forms.IntegerField(required=False, help_text='This will help us')

    class Meta:
        model = User
        fields = ('username','password1', 'password2', 'first_name', 'last_name', 'age', 'email', 'postal_code')


class MyBidsForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ('bidder', 'offer', 'amount')
