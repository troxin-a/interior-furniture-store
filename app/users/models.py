from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="users_img", blank=True, null=True, verbose_name="Аватар")

    class Meta:
        db_table = "user"
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.username
