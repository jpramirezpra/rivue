from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<str:productId>', views.product, name='product'),
    path('category/<str:catId>', views.category, name='category'),
    path('categorylist', views.categoryList, name='categoryList')
]