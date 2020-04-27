import django
django.setup()

from garb.tests.templatetags.garb_menu import GarbMenuTestCase
from garb.tests.templates.login import GarbLoginTestCase
from garb.tests.config import ConfigTestCase
from django.test.runner import DiscoverRunner 

class NoDbTestRunner(DiscoverRunner):
    """A test garb runner that does not set up and tear down a database."""

    def setup_databases(self):
        """Overrides DjangoTestGarbRunner"""
        pass

    def teardown_databases(self, *args):
        """Overrides DjangoTestGarbRunner"""
        pass


class GarbTestRunner(DiscoverRunner):
    pass
