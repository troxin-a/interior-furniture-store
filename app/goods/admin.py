from django.contrib import admin

from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Класс для отображения модели в админке"""

    # Автоматическое заполнение поля slug по полю name
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """Класс для отображения модели в админке"""

    # Автоматическое заполнение поля slug по полю name
    prepopulated_fields = {"slug": ("name",)}
    # Отображение продуктов в виде таблицы с назначенными полями
    list_display = ["name", "quantity", "price", "discount"]
    # Изменяемые поля в таблице
    list_editable = ["quantity", "price", "discount"]
    # Поиск в таблице по указанным полям
    search_fields = ["name", "description"]
    # Фильтрация в таблице по указанным полям
    list_filter = ["discount", "quantity", "category"]
    # Последовательность отображения полей в товаре
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]
