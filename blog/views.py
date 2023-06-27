from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def blog_view(request, slug):
    """ post details """
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug)
    # recent_articles = Article.objects.all()[:2]
    context = {
        'article': article,
        # 'recent_articles': recent_articles,
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


def category_detail(request, pk=None):
    """ reverse relation to access categories articles """
    category = get_object_or_404(Category, id=pk)
    # article = category.aritcles_set.all()
    article = category.articles.all()
    context = {
        'articles': article,
        'navbar': 'post_list',
    }
    return render(request, 'blog/post-list.html', context)
