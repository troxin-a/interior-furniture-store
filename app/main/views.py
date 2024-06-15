from django.shortcuts import render

from goods.models import Products


def index(request):

    goods = Products.objects.order_by("?")

    goods_for_sale = goods.filter(discount__gt=0)[:3]
    goods_for_catalog = goods[:6]

    context = {
        'title': "Главная страница магазина ИНТЕРЬЕР",
        'top_content': "Всё, чего заслуживает ваш дом",
        'goods_for_sale': goods_for_sale,
        'goods': goods_for_catalog,
    }
    return render(request, 'main/index.html', context)


def catalog(request):
    context = {
        'title': "Каталог",
    }
    return render(request, 'main/index.html', context)

def cart(request):
    context = {
        'title': "Корзина",
    }
    return render(request, 'main/index.html', context)
