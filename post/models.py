from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Essay(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

class Album(models.Model):
    image = models.ImageField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc

class File(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    myfile = models.FileField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc