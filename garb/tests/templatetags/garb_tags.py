from django.test import TestCase
from garb.templatetags.garb_tags import garb_url_exists
from django.urls import reverse, resolve

class GarbTagsTestCase(TestCase):

    def test_garb_tag_urlpath_exists(self):
        self.assertTrue(garb_url_exists('admin:login'))
        self.assertFalse(garb_url_exists('password_reset'))