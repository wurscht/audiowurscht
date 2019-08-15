from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    user = models.ManyToManyField(User)
    title = models.CharField(max_length=100, default="unknown")
    artist = models.CharField(max_length=100, default="unknown")
    album = models.CharField(max_length=100, default="unknown")
    path = models.FileField(upload_to="media/")
    tracknumber = models.CharField(max_length=100, default="unknown")

    def __str__(self):
        return self.name
