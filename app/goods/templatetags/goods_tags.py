from django.utils.http import urlencode
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    # query = {k:v for k, v in query.items() if v}
    return urlencode(query)
    