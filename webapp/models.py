from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=30, unique=True, default="key")
    picture = models.FileField(upload_to="media/profile_pictures")

    def __str__(self):
        return self.user.username


class Song(models.Model):
    user = models.ManyToManyField(User, related_name="user_songs")
    title = models.CharField(max_length=100, default="unknown")
    artist = models.CharField(max_length=100, default="unknown")
    album = models.CharField(max_length=100, default="unknown")
    path = models.FileField(upload_to="media/")
    tracknumber = models.CharField(max_length=100, default="unknown")
    picture = models.CharField(max_length=1000, default="no picture", null=True)

    def __str__(self):
        return self.title
