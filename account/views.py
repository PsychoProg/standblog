from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    """ user login operation """
    if request.user.is_authenticated:
        # no login form if user is authenticated
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("done successfully")
            return redirect('home')

    # render the login form if request is not POST.
    return render(request, 'account/login.html')


def logout_view(request):
    """ log out user """
    logout(request)
    return redirect('home')


def register_view(request):
    """ user registration operation """
    return render(request, 'account/register.html')
