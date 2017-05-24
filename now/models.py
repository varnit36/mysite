from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000)
    text = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)

