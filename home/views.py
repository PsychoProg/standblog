from django.shortcuts import render


def home(request):
    """ home page function"""
    context = {}
    return render(request, "home/index.html", context)
