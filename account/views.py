from django.shortcuts import render


def login(request):
    context = {}
    return render(request, 'account/login.html', context)
