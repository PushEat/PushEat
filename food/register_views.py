from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from forms import SignUpForm


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'users/users_login.html')
    else:
        form = SignUpForm()
    return render(request, 'users/user_register.html', {'form': form})