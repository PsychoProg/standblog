from django.shortcuts import render
from blog.models import Article


def home(request):
    """ home page function"""
    # articles = Article.objects.all()
    # use querySet and filter
    # articles = Article.objects.filter(status=True)
    articles = Article.objects.publish()    # func name
    recent_articles = Article.objects.all()[:3]
    context = {
        'articles': articles,
        'recent_articles': recent_articles,
        'navbar': 'home',
    }
    return render(request, "home/index.html", context)
