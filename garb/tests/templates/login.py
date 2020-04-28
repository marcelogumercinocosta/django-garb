from django.conf import settings
from garb.tests.mixins import UserTestCaseMixin


class GarbLoginTestCase(UserTestCaseMixin):
    def test_not_is_authenticated(self):
        self.client.logout()
        self.get_response(url="/")
        self.assertContains(self.response, '<i class="fas fa-sign-in-alt"> </i>LOGAR')

    def test_admin_is_authenticated(self):
        self.client.logout()
        self.login_superuser()
        self.get_response(url="/")
        self.assertContains(self.response,'<i class="fas fa-sign-out-alt"> </i>Sair')
        self.assertContains(self.response, self.superuser.username)

    def test_menu_user_is_authenticated(self):
        self.client.logout()
        self.login_user()
        self.get_response(url="/")
        self.assertContains(self.response,'<i class="fas fa-sign-out-alt"> </i>Sair')
        self.assertContains(self.response, self.user.username)
        