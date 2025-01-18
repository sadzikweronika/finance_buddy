from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

    # Rozwiązanie konfliktu poprzez nadanie related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Zmień nazwę relacji, aby uniknąć konfliktu
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Zmień nazwę relacji, aby uniknąć konfliktu
        blank=True
    )