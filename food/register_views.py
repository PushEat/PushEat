from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from food.forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base/leftBar')
    else:
        form = RegisterForm()

        args = {'form': form}
        return render(request, 'users/user_register.html', args)
