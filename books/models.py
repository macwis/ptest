from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Blacklist(models.Model):
    ip_addr = models.GenericIPAddressField()
