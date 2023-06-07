from django.db import models
# author from users
from django.contrib.auth.models import User


class Article(models.Model):
    """ articles """
    # model relationships
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    # set articles on home app template

    def __str__(self):
        return f"title: {self.title}"
