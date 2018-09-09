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
