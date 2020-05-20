from django import template
from django.urls import NoReverseMatch, Resolver404, resolve, reverse
from garb.config import get_config

register = template.Library()

@register.filter(name='garb_title')
def garb_title(title):
    value = get_config('PROJECT_NAME')
    if title:
        return "{0} | {1}".format(str(title), str(value).upper())
    else:
        return str(value).upper()

@register.filter(name='garb_url_exists')
def garb_url_exists(url):
    """Returns True for successful resolves()'s."""
    try:
        return bool(resolve(reverse(url)))
    except NoReverseMatch:
        return False
    except Resolver404:
        return False