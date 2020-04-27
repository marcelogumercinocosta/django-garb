from django.contrib.admin import ModelAdmin
from django.conf import settings
from garb.config import default_config, get_config
from garb.tests.mixins import UserTestCaseMixin


class ConfigTestCase(UserTestCaseMixin):
    def test_garb_config_when_not_defined(self):
        try:
            del settings.GARB_CONFIG
        except AttributeError:
            pass
        default_garb_config = default_config()
        self.assertEqual(get_config('PROJECT_NAME'), default_garb_config['PROJECT_NAME'])

        # Defined as None, should also use fallback
        project_name = None
        settings.GARB_CONFIG = {
            'PROJECT_NAME': project_name
        }
        self.assertEqual(get_config('PROJECT_NAME'), default_garb_config['PROJECT_NAME'])

    def test_garb_config_when_defined_but_no_key(self):
        settings.GARB_CONFIG = {
            'RANDOM_KEY': 123
        }
        default_garb_config = default_config()
        self.assertEqual(get_config('PROJECT_NAME'), default_garb_config['PROJECT_NAME'])
        # Defined as empty, should stay empty
        project_name = ''
        settings.GARB_CONFIG = {
            'PROJECT_NAME': project_name
        }
        self.assertEqual(get_config('PROJECT_NAME'), project_name)

    def test_garb_config_when_defined(self):
        project_name = 'BLOG GARB'
        settings.GARB_CONFIG = {
            'PROJECT_NAME': project_name
        }
        self.assertEqual(get_config('PROJECT_NAME'), project_name)

    def test_django_modeladmin_overrides(self):
        self.assertEqual(ModelAdmin.actions_on_top, False)
        self.assertEqual(ModelAdmin.actions_on_bottom, True)
        self.assertEqual(ModelAdmin.list_per_page, get_config('LIST_PER_PAGE'))