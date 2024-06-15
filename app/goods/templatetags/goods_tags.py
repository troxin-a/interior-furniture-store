from django import template

from goods.models import Products


register = template.Library()


@register.simple_tag()
def tag_goods():
    return Products.objects.order_by("?")
    