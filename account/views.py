from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    """ user login operation """
    if request.user.is_authenticated:
        # no login form if user is authenticated
        return redirect('home:home_url')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("done successfully")
            return redirect('home:home_url')

    # render the login form if request is not POST.
    return render(request, 'account/login.html')


def logout_view(request):
    """ log out user """
    logout(request)
    return redirect('home:home_url')


def register_view(request):
    """ user registration operation """
    context = {'errors': []}
    if request.user.is_authenticated:
        # no login form if user is authenticated
        return redirect('home:home_url')

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # error handling
        if password1 != password2:
            context['errors'].append('passwords does not match!')
            return render(request, 'account/register.html', context)

        user = User.objects.create(username=username, password=password1, email=email)
        # login user after registration
        login(request, user)
        return redirect('home:home_url')

    return render(request, 'account/register.html')
