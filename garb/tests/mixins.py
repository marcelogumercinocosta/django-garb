from multiprocessing.connection import Client
from random import randint

from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.core.management import CommandError, call_command
from django.test import TestCase
from django.urls import reverse
from django.views.generic import ArchiveIndexView
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from garb.tests.models import BlogComment

class UserTestCaseMixin(TestCase):
    superuser = None
    user = None

    def login_superuser(self):
        if not self.superuser:
            self.superuser = self.create_superuser()
        # file deepcode ignore NoHardcodedPasswords: tests
        self.client.login(username=self.superuser.username, password='Senha231.')

    def create_superuser(self):
        return User.objects.create_superuser('admin-%s' % str(randint(1, 9999)), 'test@test.com', 'Senha231.')

    def create_user(self):
        user = User.objects.create_user('user-%s' % str(randint(1, 9999)), 'test2@test2.com', 'Senha123.')
        user.is_staff = True
        user.save()
        return user

    def login_user(self):
        if not self.user:
            self.user = self.create_user()
        # file deepcode ignore NoHardcodedPasswords: tests
        self.client.login(username=self.user.username, password='Senha123.')

    def login_user_permission(self):
        self.login_user()
        content_type = ContentType.objects.get_for_model(BlogComment, for_concrete_model=False)
        Permission.objects.create(codename='can_hire', name='Can hire comments', content_type=content_type)
        permission = Permission.objects.get(codename='can_hire')
        self.user.user_permissions.add(permission)

    def get_response(self, url=None):
        url = url or reverse('admin:index')
        self.response = self.client.get(url)


class ModelsTestCaseMixin(TestCase):
    def _pre_setup(self):
        self.saved_INSTALLED_APPS = settings.INSTALLED_APPS
        self.saved_DEBUG = settings.DEBUG
        test_app = 'garb.tests'
        settings.INSTALLED_APPS = tuple(
            list(self.saved_INSTALLED_APPS) + [test_app] 
        )
        settings.DEBUG = True
        try:
            call_command('syncdb', verbosity=0, interactive=False)
        except CommandError:
            pass
        super(ModelsTestCaseMixin, self)._pre_setup()

    def _post_teardown(self):
        settings.INSTALLED_APPS = self.saved_INSTALLED_APPS
        settings.DEBUG = self.saved_DEBUG
        super(ModelsTestCaseMixin, self)._post_teardown()

