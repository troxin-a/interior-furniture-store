from django.db import models

from goods.models import Products
from users.models import User


class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Пользователь")
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        db_table = "cart"
        verbose_name = "Корзину"
        verbose_name_plural = "Корзины"


    objects = CartQuerySet().as_manager()

    def __str__(self):
        return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"

    def products_price(self):
        return round(self.product.get_sell_price() * self.quantity)
