from django.conf import settings
from django.contrib.auth.models import Permission
from django.urls import reverse, resolve
from django.utils.encoding import force_text as force_unicode
from garb.tests.models import *
from garb.tests.urls import *
from garb.templatetags.garb_menu import get_menu, Menu, ItemLink, ItemLinkModel
from garb.tests.mixins import ModelsTestCaseMixin, UserTestCaseMixin


class GarbMenuTestCase(ModelsTestCaseMixin, UserTestCaseMixin):
    def setUp(self):
        self.setUpConfig()
        self.login_superuser()

    def setUpConfig(self):
        settings.GARB_CONFIG = getattr(settings, 'GARB_CONFIG', {})
        settings.GARB_CONFIG.update({
            'MENU': [
                { 'label': 'menu1',  'icon': 'fa-user-plus',  'route': 'blog/', 'auth':'all' },
                { 'label': 'menu2',  'icon': 'fa-user-plus',
                    'sub_itens':[
                        { 'model':'garb.blog'},
                        { 'model':'garb.blogcomment'},
                    ]
                },
                { 'label': 'menu3',  'icon': 'fa-user-plus', 'auth':'all',
                    'sub_itens':[
                        { 'label': 'sub1', 'route': 'www.uol.com.br', 'target':'_blank' },
                        { 'label': 'sub2', 'route': 'blog1/', 'permission': 'garb.can_hire', },
                        { 'label': 'sub3', 'route': 'blog2/', 'auth':'yes' },
                        { 'label': 'sub4', 'route': 'blog3/', 'auth':'no' },
                    ]
                }
            ],
        })

    def make_menu_from_response(self):
        return get_menu(self.response.context, self.response._request)

    def test_index(self):
        self.client.logout()
        self.get_response(url="/")

    def test_menu_admin(self):
        self.client.logout()
        self.login_superuser()
        self.get_response()
        app_label = 'garb'
        mc = settings.GARB_CONFIG['MENU']
        menu = self.make_menu_from_response()
        self.assertEqual(len(menu), len(mc))

        # as string
        i = 0
        self.assertEqual(menu[i].label, mc[i]['label'])
        self.assertEqual(menu[i].route, mc[i]['route'])
        self.assertEqual(menu[i].icon, 'fa-user-plus')
        self.assertEqual(menu[i].auth, 'all')

        i += 1 # as dict
        self.assertEqual(type(menu[i].childrens[0]), ItemLinkModel)
        self.assertEqual(len(menu[i].childrens), len(mc[i]['sub_itens']))
        self.assertEqual(menu[i].icon, mc[i]['icon'])
        self.assertEqual(menu[i].childrens[0].route, resolve(reverse('admin:%s_%s_changelist' % (app_label,'blog'))).route)
        self.assertEqual(menu[i].childrens[1].route, resolve(reverse('admin:%s_%s_changelist' % (app_label,'blogcomment'))).route)

        i += 1 # as dict      
        self.assertEqual(menu[i].auth, 'all')
        self.assertEqual(menu[i].childrens[0].auth, 'all')
        self.assertEqual(type(menu[i].childrens[0]), ItemLink)
        self.assertEqual(menu[i].childrens[0].target, '_blank')
        self.assertEqual(menu[i].childrens[1].auth, 'all')
        self.assertEqual(menu[i].childrens[2].auth, 'yes')
        self.assertEqual(menu[i].label, mc[i]['label'])
        self.assertEqual(len(menu[i].childrens), 3)
        self.assertEqual(len(menu[i].childrens), len(mc[i]['sub_itens'])-1)

    def test_menu_user(self):
        self.client.logout()
        self.login_user()
        self.get_response()
        mc = settings.GARB_CONFIG['MENU']
        menu = self.make_menu_from_response()
        self.assertEqual(len(menu), len(mc)-1)

        i = 0
        self.assertEqual(menu[i].label, mc[i]['label'])
        self.assertEqual(menu[i].route, mc[i]['route'])
        self.assertEqual(menu[i].icon, 'fa-user-plus')
        self.assertEqual(menu[i].auth, 'all')

        i += 1 # as dict      
        self.assertEqual(menu[i].auth, 'all')
        self.assertEqual(menu[i].childrens[0].auth, 'all')
        self.assertEqual(type(menu[i].childrens[0]), ItemLink)
        self.assertEqual(menu[i].childrens[0].target, '_blank')
        self.assertEqual(menu[i].childrens[1].auth, 'yes')
        self.assertEqual(menu[i].label, mc[i+1]['label'])
        self.assertEqual(len(menu[i].childrens), 2)
        self.assertEqual(len(menu[i].childrens), len(mc[i+1]['sub_itens'])-2)
        self.assertEqual(menu[i].childrens[0].label, 'sub1')
        self.assertEqual(menu[i].childrens[1].label, 'sub3')


    def test_menu_not_authenticated(self):
        self.client.logout()
        self.get_response(url="/")
        mc = settings.GARB_CONFIG['MENU']
        menu = self.make_menu_from_response()
        self.assertEqual(len(menu), len(mc)-1)

        i = 0
        self.assertEqual(menu[i].label, mc[i]['label'])
        self.assertEqual(menu[i].route, mc[i]['route'])
        self.assertEqual(menu[i].icon, 'fa-user-plus')
        self.assertEqual(menu[i].auth, 'all')

        i += 1 # as dict      
        self.assertEqual(menu[i].auth, 'all')
        self.assertEqual(menu[i].childrens[0].auth, 'all')
        self.assertEqual(type(menu[i].childrens[0]), ItemLink)
        self.assertEqual(menu[i].childrens[0].target, '_blank')
        self.assertEqual(menu[i].childrens[1].auth, 'no')
        self.assertEqual(menu[i].label, mc[i+1]['label'])
        self.assertEqual(len(menu[i].childrens), 2)
        self.assertEqual(len(menu[i].childrens), len(mc[i+1]['sub_itens'])-2)
        self.assertEqual(menu[i].childrens[0].label, 'sub1')
        self.assertEqual(menu[i].childrens[1].label, 'sub4')

    def test_menu_user_permission(self):
        self.client.logout()
        self.login_user_permission()
        self.get_response()
        mc = settings.GARB_CONFIG['MENU']
        menu = self.make_menu_from_response()
        self.assertEqual(len(menu), len(mc)-1)

        i = 0
        self.assertEqual(menu[i].label, mc[i]['label'])
        self.assertEqual(menu[i].route, mc[i]['route'])
        self.assertEqual(menu[i].icon, 'fa-user-plus')
        self.assertEqual(menu[i].auth, 'all')

        i += 1 # as dict      
        self.assertEqual(menu[i].auth, 'all')
        self.assertEqual(menu[i].childrens[0].auth, 'all')
        self.assertEqual(type(menu[i].childrens[0]), ItemLink)
        self.assertEqual(menu[i].childrens[0].target, '_blank')
        self.assertEqual(menu[i].childrens[1].permission, 'garb.can_hire')
        self.assertEqual(menu[i].childrens[2].auth, 'yes')
        self.assertEqual(menu[i].label, mc[i+1]['label'])
        self.assertEqual(len(menu[i].childrens), 3)
        self.assertEqual(len(menu[i].childrens), len(mc[i+1]['sub_itens'])-1)
        self.assertEqual(menu[i].childrens[0].label, 'sub1')
        self.assertEqual(menu[i].childrens[1].label, 'sub2')
        self.assertEqual(menu[i].childrens[2].label, 'sub3')

