import django
django.setup()

from garb.tests.templatetags.garb_menu import GarbMenuTestCase
from garb.tests.templatetags.garb_tags import GarbTagsTestCase
from garb.tests.templatetags.garb_list import GarbListTestCase
from garb.tests.templates.login import GarbLoginTestCase
from garb.tests.config import ConfigTestCase, ConfigWithModelsTestCase
from django.test.runner import DiscoverRunner


class GarbTestRunner(DiscoverRunner):
    pass
