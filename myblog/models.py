from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


class CustomUser(AbstractUser):
    pass
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    subject = models.CharField(max_length=250)
    entry = models.CharField(max_length=4096)
    date_time = models.DateTimeField(default=datetime.now)
    last_update = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.author.username + " - " + self.subject
