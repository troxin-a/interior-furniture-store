from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Products


def catalog(request, category_slug):

    page_number = request.GET.get('page', 1)

    if category_slug=="all":
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 6)
    current_page = paginator.page(page_number)

    context = {
        'title': 'Каталог',
        'goods': current_page,
        "slug_url": category_slug,
    }
    return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug):

    prod = Products.objects.get(slug=product_slug)

    context = {
        'product': prod,
    }
    return render(request, 'goods/product.html', context=context)
