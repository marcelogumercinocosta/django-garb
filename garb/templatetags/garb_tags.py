from django import template
from garb.config import get_config

register = template.Library()
simple_tag = register.simple_tag

@register.filter(name='garb_title')
def garb_title(title):
    value = get_config('PROJECT_NAME')
    if title:
        return "{0} | {1}".format(str(title), str(value).upper())
    else:
        return str(value).upper()
