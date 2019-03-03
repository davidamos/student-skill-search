# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here

    is_searching = models.BooleanField()

    def __str__(self):
        return self.email
