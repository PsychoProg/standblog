from django.shortcuts import render, get_object_or_404
from .models import Article


def blog_view(request, pk):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, id=pk)
    context = {
        'article': article,
    }
    return render(request, 'blog/post-details.html', context)
