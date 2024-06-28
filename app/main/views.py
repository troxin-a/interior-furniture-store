from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная страница магазина ИНТЕРЬЕР",
    }
    return render(request, "main/index.html", context)


def catalog(request):
    context = {
        "title": "Каталог",
    }
    return render(request, "main/index.html", context)


def cart(request):
    context = {
        "title": "Корзина",
    }
    return render(request, "main/index.html", context)
