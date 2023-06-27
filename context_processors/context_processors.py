from blog.models import Article, Category


def recent_articles(request):
    """ for global use """
    # Note: define this function in settings.py > Templates > context_processors
    recent = Article.objects.order_by('-created')[:3]
    context = {
        'recent_articles': recent,
    }

    return context


def category(request):
    """ show categories in sidebar """
    categories = Category.objects.order_by('-created')[:5]
    # category = Category.objects.all().order_by('-created')
    context = {
        'categories': categories,
    }
    return context
