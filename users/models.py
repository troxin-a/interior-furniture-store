from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users_img", blank=True, null=True, verbose_name="Аватар")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Номер телефона")
    delivery_address = models.CharField(max_length=100, blank=True, verbose_name="Адрес доставки")

    class Meta:
        db_table = "user"
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.username
