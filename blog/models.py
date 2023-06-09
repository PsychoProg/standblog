from django.db import models
# author from users
from django.contrib.auth.models import User
# import manager
from . import managers
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    """ articles """
    # model relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="articles")
    title = models.CharField(max_length=70, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles", help_text="choose an image in right size.")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """ generate slug """
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        """ absolute url """
        # return reverse('blog:post_url', kwargs={'title': self.title})
        return reverse('blog:post_url', kwargs={'slug': self.slug})

    # Article objects
    objects = managers.ArticleManager()

    # rewriting get_queryset
    # objects = models.Manager()
    # custom_manager = managers.ArticleManager()

    # set articles on home app template

    def __str__(self):
        return f"title: {self.title}, id: {self.id}"

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        # order objects base on update date
        # ordering = ('-created',)
        ordering = ('-updated', '-created')


class Comment(models.Model):
    """ handle comments and replies """
    # ManyToONe (each Article has Many comments)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")

    # ManyToONe (each User has Many comments)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    # Replies: each comments has many replies
    # 'self' is an object of this class
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name="replies")

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

    class Meta:
        ordering = ('-created',)


class Contact(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        ordering = ('-created',)
