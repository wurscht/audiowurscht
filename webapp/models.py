from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100, default="unknown")
    song = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name
