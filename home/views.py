from django.shortcuts import render
from blog.models import Article


def home(request):
    """ home page function"""
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, "home/index.html", context)
