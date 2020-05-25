from builtins import range
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from garb.templatetags.garb_list import garb_list_filter_select, pagination, paginator_info, paginator_number, get_for_one_string
from garb.tests.mixins import UserTestCaseMixin
from garb.tests.models import *
from django.conf import settings

app_label = test_app_label()

class GarbListTestCase(UserTestCaseMixin):
    changelist = None
    blog = None

    def get_changelist(self):
        self.get_response(reverse('admin:%s_blog_changelist' % app_label))
        self.changelist = self.response.context_data['cl']

    def setUp(self):
        self.login_superuser()
        self.blog = Blog(name='Test')
        self.blog.save()
        self.get_changelist()

    def test_paginator_number(self):
        output = paginator_number(self.changelist, 100)
        self.assertTrue('100' in output)

        output = paginator_number(self.changelist, '.')
        self.assertTrue('...' in output)

        output = paginator_number(self.changelist, 0)
        self.assertTrue('active' in output)

    def test_paginator_info(self):
        output = paginator_info(self.changelist)
        self.assertEqual('1 - 1', output)

    def test_pagination_one_page(self):
        pg = pagination(self.changelist)
        self.assertEqual(pg['cl'], self.changelist)
        self.assertEqual(pg['page_range'], [])
        self.assertEqual(pg['pagination_required'], False)

    def test_pagination_many_pages(self):
        per_page_original = ModelAdmin.list_per_page
        ModelAdmin.list_per_page = 10
        for x in range(25):
            blog = Blog(name='Test %d' % x)
            blog.save()

        self.get_changelist()
        pg = pagination(self.changelist)
        ModelAdmin.list_per_page = per_page_original
        self.assertEqual(pg['cl'], self.changelist)
        self.assertEqual(len(pg['page_range']), 3)
        self.assertEqual(pg['pagination_required'], True)

    def test_garb_list_filter_select(self):
        filter_matches = (self.blog.pk, self.blog.name)
        self.assertEqual(len(self.changelist.filter_specs), 2)

        for i, spec in enumerate(self.changelist.filter_specs):
            filter_output = garb_list_filter_select(self.changelist, spec)
            self.assertTrue('value="%s"' % filter_matches[i] in filter_output)
    
    def test_get_for_one_string(self):
        filter_output = get_for_one_string(self.changelist.list_filter)
        self.assertEqual(filter_output, 'Id | Name')