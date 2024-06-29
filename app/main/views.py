from django.shortcuts import render


def index(request):
    context = {
        "title": "Главная страница магазина ИНТЕРЬЕР",
    }
    return render(request, "main/index.html", context)
