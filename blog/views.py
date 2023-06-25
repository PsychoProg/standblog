from django.shortcuts import render, get_object_or_404
from .models import Article


def blog_view(request, slug):
    """ post details """
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug)
    recent_articles = Article.objects.all()[:2]
    context = {
        'article': article,
        'recent_articles': recent_articles,
        'navbar': 'post',
    }
    return render(request, 'blog/post-details.html', context)


def post_list(request):
    article = Article.objects.all()
    context = {
        'articles': article,
        'navbar': 'post_list'
    }
    return render(request, 'blog/post-list.html', context)
