from django.contrib import admin

from carts.models import Cart

# admin.site.register(Cart)


class CartTabAdmin(admin.TabularInline):
    """Класс для отображения модели в карточке другой модели"""

    model = Cart
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1  # Дополнительная строчка для добавления


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Класс для отображения модели в админке"""

    # Отображение продуктов в виде таблицы с назначенными полями
    # user_display берется из метода данного класса
    list_display = ["user_display", "product", "quantity", "created_timestamp"]
    # Фильтры таблицы по указанным полям
    list_filter = ["created_timestamp", "user", "product"]

    def user_display(self, obj):
        """ Метод для переопределения отображаемых полей в таблице админки"""
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
