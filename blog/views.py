from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from .forms import Contact

def blog_view(request, slug):
    """ post details """
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug)
    # recent_articles = Article.objects.all()[:2]

    # comment form
    if request.method == "POST":
        body = request.POST.get('body')
        # create a comment in db
        Comment.objects.create(body=body, article=article, user=request.user)

    context = {
        'article': article,
        # 'recent_articles': recent_articles,
        'navbar': 'post',
    }
    return render(request, 'blog/post-details.html', context)


def post_list(request):
    """ list articles with pagination """
    # article = Article.objects.all()
    article = Article.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(article, 2)
    objects_list = paginator.get_page(page_num)

    context = {
        # 'articles': article,
        'articles': objects_list,
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


def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    # pagination
    page_num = request.GET.get('page')
    paginator = Paginator(article, 1)
    objects_list = paginator.get_page(page_num)

    context = {
        'articles': objects_list,
    }
    return render(request, 'blog/post-list.html', context)


def contact(request):
    form = Contact()
    context = {'forms': form}
    return render(request, 'blog/contact.html', context)
