from django import forms
from django.core import mail
from django.contrib.auth.models import Permission
from django.template.loader import render_to_string
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from garb.config import default_config, get_config
from garb.forms import GarbForm, GarbModelForm, PreviewForm
from garb.tests.mixins import UserTestCaseMixin
from garb.tests.models import Blog, Category


class SampleForm(GarbForm):
    title = forms.CharField()
    published_on = forms.DateField(required=False)

    class Meta:
        fieldsets = (("Content", {"fields": ("title", "published_on")}),)
        row_attrs = {"title": {"class": "wide"}}
        submit_text = "Save"


class SamplePreviewForm(PreviewForm):
    title = forms.CharField()


class BlogModelForm(GarbModelForm):
    class Meta:
        model = Blog
        fieldsets = (("Content", {"fields": ("name", "category")}),)


class GarbFormCompatibilityTests(TestCase):
    def test_fieldsets_and_row_attributes(self):
        form = SampleForm(data={"title": "Post", "published_on": "2026-08-20"})
        self.assertTrue(form.is_valid())
        fieldset = next(iter(form.fieldsets))
        self.assertEqual(fieldset.name, "Content")
        self.assertEqual(fieldset.errors, {})
        list(fieldset)
        title = form["title"]
        self.assertIn("wide", title.row_attrs["class"])
        self.assertIn("required", title.row_attrs["class"])
        self.assertIn("vDateField", form.fields["published_on"].widget.attrs["class"])

    def test_model_form_infers_fields_from_fieldsets(self):
        form = BlogModelForm()
        self.assertEqual(list(form.fields), ["name", "category"])

    def test_preview_form_detects_positional_data(self):
        form = SamplePreviewForm({"title": "Draft", "submit": "preview"})
        self.assertTrue(form.preview)
        self.assertFalse(form.is_valid())


class AdminFlowTests(UserTestCaseMixin):
    def setUp(self):
        self.login_superuser()
        self.category = Category.objects.create(name="Technology")
        self.blog = Blog.objects.create(
            name="Post 1",
            subtitle="Modern Django",
            content="Test content",
            category=self.category,
            published_at=timezone.now(),
        )

    def assert_page(self, route, *args):
        response = self.client.get(reverse(route, args=args))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, get_config("PROJECT_NAME").upper())
        return response

    def test_primary_admin_pages_render(self):
        self.assert_page("admin:index")
        self.assert_page("admin:tests_blog_changelist")
        self.assert_page("admin:tests_blog_add")
        self.assert_page("admin:tests_blog_change", self.blog.pk)
        self.assert_page("admin:tests_blog_delete", self.blog.pk)
        self.assert_page("admin:tests_blog_history", self.blog.pk)

    def test_search_filter_and_pagination_render(self):
        response = self.client.get(
            reverse("admin:tests_blog_changelist"),
            {"q": "Post", "category__id__exact": self.category.pk},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Post 1")
        self.assertContains(response, "search-filter")

    def test_create_change_and_delete_flow(self):
        add_url = reverse("admin:tests_blog_add")
        response = self.client.post(
            add_url,
            {
                "name": "Created",
                "subtitle": "Through admin",
                "content": "Body",
                "category": self.category.pk,
                "deleted": "",
                "comments-TOTAL_FORMS": "0",
                "comments-INITIAL_FORMS": "0",
                "comments-MIN_NUM_FORMS": "0",
                "comments-MAX_NUM_FORMS": "1000",
                "_save": "Save",
            },
        )
        self.assertEqual(response.status_code, 302)
        created = Blog.objects.get(name="Created")
        response = self.client.post(
            reverse("admin:tests_blog_delete", args=(created.pk,)),
            {"post": "yes"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Blog.objects.filter(pk=created.pk).exists())

    def test_logout_uses_post_and_renders_confirmation(self):
        response = self.client.post(reverse("admin:logout"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, get_config("PROJECT_NAME").upper())


class AuthenticationAndPermissionTests(UserTestCaseMixin):
    def test_anonymous_admin_request_redirects_to_login(self):
        response = self.client.get(reverse("admin:tests_blog_changelist"))
        self.assertRedirects(
            response,
            f'{reverse("admin:login")}?next={reverse("admin:tests_blog_changelist")}',
        )

    def test_staff_user_without_permission_cannot_see_or_open_model(self):
        self.login_user()
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "BLOGS")
        response = self.client.get(reverse("admin:tests_blog_changelist"))
        self.assertEqual(response.status_code, 403)

    def test_password_change_and_reset_templates_render(self):
        self.login_superuser()
        response = self.client.get(reverse("admin:password_change"))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("password_reset"), {"email": self.superuser.email})
        self.assertRedirects(response, reverse("password_reset_done"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("/accounts/reset/", mail.outbox[0].body)

    def test_public_error_templates_render_valid_shell(self):
        for status in (403, 404, 500):
            html = render_to_string(f"{status}.html")
            self.assertIn(f"<span>{str(status)[0]}</span>", html)
            self.assertEqual(html.count('<div class="breadcrumbs">'), 1)


class PublicConfigurationTests(TestCase):
    @override_settings(GARB_CONFIG={"PROJECT_NAME": "Custom"})
    def test_partial_configuration_is_merged_with_defaults(self):
        config = get_config()
        self.assertEqual(config["PROJECT_NAME"], "Custom")
        self.assertEqual(config["THEME"], default_config()["THEME"])

    def test_permission_codename_exists_for_visual_fixture(self):
        self.assertTrue(Permission.objects.filter(codename="can_hire").exists())
