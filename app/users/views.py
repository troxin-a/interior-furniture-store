from django.shortcuts import render

from goods.models import Products


def login(request):
    context = {
        'title': 'Авторизация'
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Регистрация'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Профиль'
    }

    return render(request, 'users/profile.html', context)

def cart(request):
    goods = Products.objects.order_by("?")

    goods = goods.filter(discount__gt=0)[:3]

    context = {
        'title': 'Корзина',
        'goods': goods,
    }

    return render(request, 'users/cart.html', context)


def logout(request):
    context = {
        'logout': 'Выход'
    }

    return render(request, '', context)
