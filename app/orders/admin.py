from django.contrib import admin

from orders.models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabAdmin(admin.TabularInline):
    model = OrderItem
    # Последовательность отображения полей в карточке
    fields = "product", "name", "price", "quantity"
    search_fields = ("product", "name",)
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = ("order", "product", "name",)


class OrderTabAdmin(admin.TabularInline):
    model = Order

    # Последовательность отображения полей в карточке
    fields = ("status", "created_timestamp",)
    search_fields = ("created_timestamp",)
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    # Отображение продуктов в виде таблицы с назначенными полями
    # user_display берется из метода данного класса
    list_display = ("id", "user", "status", "created_timestamp",)
    # Поля, по которым ведется поиск
    search_fields = ("id",)
    # Поля только для чтения
    readonly_fields = ("created_timestamp",)
    # Поля для фильтрации
    list_filter = ("status",)
    # Подключаются элементы по ForeignKey
    inlines = (OrderItemTabAdmin,)
