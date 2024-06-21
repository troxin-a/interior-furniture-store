from django.shortcuts import render
from django.core.paginator import Paginator

from goods.utils import get_queryset_or_404, q_search
from goods.models import Products


def catalog(request, category_slug=None):

    page_number = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    on_sale = request.GET.get('on_sale', None)
    query = request.GET.get('q', None)

    if category_slug=="all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_queryset_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)        
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6)
    current_page = paginator.page(page_number)

    context = {
        'title': 'Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug):

    prod = Products.objects.get(slug=product_slug)

    context = {
        'product': prod,
    }
    return render(request, 'goods/product.html', context=context)
