from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "категорию"
        verbose_name_plural = "Категории"



class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Изображение")
    price = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name="Цена")
    discount = models.SmallIntegerField(default=0, blank=True, null=True, verbose_name="Скидка в %")
    quantity = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Количество")
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "Товары"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.name

    def get_id(self) -> str:
        return str(self.id).rjust(6, "0")

    def get_old_price(self) -> str:
        price = f"{self.price:,}".replace(',', ' ')
        return price

    def get_sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100))
        return self.price

    def get_new_price(self) -> str:
        price = self.get_sell_price()
        price = f"{price:,}".replace(',', ' ')
        return price
