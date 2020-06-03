import re
from struct import pack_into

from django import template
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import get_path_info
from django.http import HttpRequest
from django.urls import resolve, reverse
from django.urls.exceptions import NoReverseMatch

from garb.config import get_config

register = template.Library()


class ItemLink(object):

    def __init__(self, app, user, path_info):
        self.auth = 'yes'
        self.user = user
        self.path_info = path_info
        self.route = None
        self.link = None
        self.target = None
        self.collapsed = False
        for name in app:
            setattr(self, name, app[name])
        if 'sub_itens' in app:
            for sub_item in self.sub_itens:
                if (not 'auth' in sub_item) and ( 'auth' in app):
                    sub_item.update({"auth": self.auth})
            menu =  Menu(self.sub_itens, user=user, path_info=path_info).get_app_list()
            self.collapsed = True if True in [item.get_active() for item in menu ] else False
            self.childrens = menu
    
    def get_target(self):
        if self.target:
            return "target='_blank'"

    def get_chave(self):
        return re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', self.label)

    def get_active(self):
        array_path = str(self.path_info).split('/')
        if self.route and ('/'.join(array_path[0:4]) + "/").replace("//", "/") == reverse(self.route):
            return True
        return False
    
    def get_url(self):
        if self.route:
            return  reverse(self.route)
        elif self.link:
            self.target = "_blank"
            return self.link
        else:
            return "#"

    def check_perms(self):
        if hasattr(self,'permission'):
            perms = perms if isinstance(self.permission, (list, tuple)) else (self.permission,)
            if self.user.has_perms(perms):
                return self
            else:
                return None
        return self


class ItemLinkModel(ItemLink):

    def __init__(self, app, user, path_info):
        self.app_name, self.model_name = app['model'].lower().split('.')
        try:
            model = apps.get_model(self.app_name, self.model_name)
            app.update({"label": model._meta.verbose_name_plural})
            app.update({"route": 'admin:{0}_{1}_changelist'.format(self.app_name, self.model_name)})
            app.update({"auth": 'yes'})
            super().__init__(app, user, path_info)
        except NoReverseMatch:
            raise NoReverseMatch('Link para o modelo %s não existe' % repr(app['model']))
        except Exception as ex:
            msg_erro = "An exception of type {0} occurred. Arguments:{1}"
            raise Exception(msg_erro.format(type(ex).__name__, ex.args))

    def check_perms(self):
        if self.user.has_perms('admin:{0}_{1}_changelist'.format(self.app_name, self.model_name)):
            return self



class Menu(object):

    def __init__(self, app_list, path_info,  **kwargs):
        self.user = kwargs.get('user')
        self.app_list = app_list
        self.path_info = path_info

    def get_app_list(self):
        menu_principal = []
        for app in self.app_list:
            item = self.make_app(app)
            if item and not (("sub_itens" in app) and (not item.childrens)):
                menu_principal.append(item)
        return menu_principal

    def make_app(self, app):
        if isinstance(app, dict):
            app = app.copy()
            if ("model" in app) and (self.user.is_authenticated):
                return ItemLinkModel(app, self.user, self.path_info).check_perms()
            if ("label" in app) and self.has_auth_item_link(app, self.user.is_authenticated):
                    return ItemLink(app, self.user, self.path_info).check_perms()
            return False

    def has_auth_item_link(self, app, authenticated):
        if ('auth' in app ):
            if app['auth']=='all':
                return True
            if authenticated:
                if app['auth']=='yes':
                    return True
                else:
                    return False
            else:
                if app['auth']=='no':
                    return True
                else:
                    return False
        elif ("sub_itens" in app):
            return True
        return False


@register.simple_tag(takes_context=True)
def get_menu(context, request):
    app_list = get_config('MENU')
    return Menu(app_list, user=context.get('user'), path_info=request.path_info ).get_app_list()