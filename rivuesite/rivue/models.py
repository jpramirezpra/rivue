from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=15)

class Category(models.Model):
    name = models.CharField(max_length=15)
    class Meta:
        verbose_name_plural = "categories"

class ReviewLink(models.Model):
    name = models.CharField(max_length=50)

class Brand(models.Model):
    name = models.CharField(max_length=50)