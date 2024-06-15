from django.shortcuts import render

from goods.models import Products

def catalog(request):
    context = {
        'title': 'Каталог',        
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        'title': 'Продукт'
    }
    return render(request, 'goods/product.html', context)
