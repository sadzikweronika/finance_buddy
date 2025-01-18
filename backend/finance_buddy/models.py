from django.db import models
from django.contrib.auth.models import AbstractUser

class Expense(models.Model):
    name = models.CharField(max_length=255, null=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # tuples, because first value is the value which will be saved in db
    # second value is the value which is displayed to the user
    CATEGORY_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Healthcare', 'Healthcare'),
        ('Entertainment', 'Entertainment'),
        ('Others', 'Others'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Others')

    TYPE_CHOICES = [
        ('Revenue', 'Revenue'),
        ('Expense', 'Expense'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Expense')

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type} - {self.amount})"
    
    class Meta:
        db_table = "expenses"


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email']

