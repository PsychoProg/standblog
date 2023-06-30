from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Article, Category, Comment, Contact
from django.core.paginator import Paginator
from .forms import ContactForm


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


#
def contact(request):
    """ Contact-us page Comments """
    if request.method == "POST":
        # form = ContactForm(data=request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get("message"))
            # email = form.cleaned_data["email"]
            # title = form.cleaned_data["title"]
            # message = form.cleaned_data["message"]

            form.save()
            return HttpResponseRedirect(reverse('blog:contact_page_url'))
            # create object in Contact model
            # Contact.objects.create(email=email, title=title, message=message)
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})
