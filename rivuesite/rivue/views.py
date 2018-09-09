from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    context = {
        'testVar': True
    }
    return render(request, 'index.html', context)

def product(request, productId):
    product = get_object_or_404(Product, name=productId)
    context = {
        'product' : product
    }
    return render(request, 'productDetail.html', context)

def category(request, catId):
    category = get_object_or_404(Product, name=catId)
    context = {
        'product' : category
    }
    return render(request, 'categoryDetail.html')

def categoryList(request):
    return render(request, 'categoryList.html')

def handler404(request):
    return render(request, 'base/404.html', status=404)

def handler500(request):
    return render(request, 'base/500.html', status=500)
