from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')

    def __str__(self):
        return self.username
