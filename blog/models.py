from django.db import models
# author from users
from django.contrib.auth.models import User


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
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles", help_text="choose an image in right size.")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # set articles on home app template

    def __str__(self):
        return f"title: {self.title}"

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
