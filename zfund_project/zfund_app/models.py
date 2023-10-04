
from django.db import models


class User(models.Model):
    ROLE_CHOICES = [
        ('advisor', 'Advisor'),
        ('user', 'User'),
    ]

    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    advisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    products = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.name
