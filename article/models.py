from django.contrib.auth.models import User

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=64)
    thumbnail = models.ImageField(upload_to='article')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
