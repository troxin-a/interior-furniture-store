from django.utils.http import urlencode
from django import template

from goods.models import Products


register = template.Library()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)

    return urlencode(query)


@register.simple_tag
def list_products(filter):
    """
    Пользовательский тег, делает запрос и возвращает в шаблон страницы Queryset при аргументах:
    'little'. 6 случайных продуктов
    'spec_offers' 3 товара со скидкой
    """

    all_products = Products.objects.order_by("?")

    if filter == "little":
        return all_products[:6]
    if filter == "spec_offers":
        return all_products.filter(discount__gt=0)[:3]
