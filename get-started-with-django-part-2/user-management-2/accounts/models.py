from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
