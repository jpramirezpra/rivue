from django.contrib import admin

from .models import Product, Brand, ReviewLink, Category
# Register your models here.

admin.site.register([Product, Brand, ReviewLink, Category])