from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from food.models import Subscribed
from forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            age = form.cleaned_data.get('age')
            postal_code = form.cleaned_data.get('postal_code')

            user = authenticate(username=username, password=raw_password)

            sus = Subscribed(first_name=firstname, last_name=lastname,
                             age=age, postal_code=postal_code, user=user)
            sus.save()
            login(request, user)
            return render(request, 'users/users_login.html')
    else:
        form = SignUpForm()
    return render(request, 'users/user_register.html', {'form': form})
