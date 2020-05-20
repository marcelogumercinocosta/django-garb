from random import randint
from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.core.management import CommandError, call_command
from django.test import TestCase
from django.urls import reverse
from garb.tests.models import BlogComment
from django.views.generic import ArchiveIndexView

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
        permission = Permission.objects.get(codename='can_hire')
        self.user.user_permissions.add(permission)

    def get_response(self, url=None):
        url = url or reverse('admin:index')
        self.response = self.client.get(url)

