from django.shortcuts import render, get_object_or_404
from .models import Article


def blog_view(request, slug):
    """ post details """
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug)
    context = {
        'article': article,
        'navbar': 'post',
    }
    return render(request, 'blog/post-details.html', context)
