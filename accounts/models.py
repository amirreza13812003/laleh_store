from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    USER_ROLES = [
    ("admin", "Admin"),
    ("customer", "Customer"),
]
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
