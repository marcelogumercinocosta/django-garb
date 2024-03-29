from builtins import object

from django import template
from django.urls import NoReverseMatch, Resolver404, resolve, reverse
from garb.config import get_config
from django.http import HttpRequest
import re

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

#TODO: Criar Testes

@register.filter
def concatene(value1,value2):
    return str(value1) + " " + str(value2)


@register.filter
def get_for_one_string(fields_list):
    return ' | '.join(x.capitalize().replace("_", " ") for x in fields_list)


@register.filter
def get_for_two_string(lista):
    result = []
    for fildset_type, fildset in lista:
        for field in fildset['fields']:
            result.append(field)
    return ' | '.join(x.capitalize().replace("_", " ") for x in result)


@register.filter(name='settings_value')
def settings_value(name):
    return get_config(name)


@register.simple_tag
def get_verbose_name_field(object, fieldnm): 
    return object._meta.get_field(fieldnm).verbose_name

@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def remove_tags(value):
    return re.compile(r'<[^>]+>').sub('', value)