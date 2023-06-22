from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30)
    national_code = models.CharField(max_length=10)
    user_image = models.ImageField(upload_to='profiles/images', db_column='image', null=True, blank=True)

    def __str__(self):
        return self.user.username
