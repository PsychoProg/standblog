from django.db import models


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())

    # def get_queryset(self):
    #     return super(ArticleManager, self).get_queryset().filter(status=True)
    # # use this code in views: articles = Article.custom_manager.all()
    def publish(self):
        return self.filter(status=True)
