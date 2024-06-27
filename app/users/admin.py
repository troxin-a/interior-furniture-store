from django.contrib import admin

from carts.admin import CartTabAdmin
from users.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для отображения модели в админке"""

    # Отображение продуктов в виде таблицы с назначенными полями
    list_display = ["username", "first_name", "last_name", "email"]
    # Поиск в таблице по указанным полям
    search_fields = ["username", "first_name", "last_name", "email"]

    # Отображение корзины в карточке пользователя
    inlines = [CartTabAdmin]
