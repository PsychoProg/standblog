from django.shortcuts import render
from blog.models import Article


def home(request):
    """ home page function"""
    # articles = Article.objects.all()
    # use querySet and filter
    # articles = Article.objects.filter(status=True)
    articles = Article.objects.publish()    # func name
    context = {'articles': articles}
    return render(request, "home/index.html", context)
