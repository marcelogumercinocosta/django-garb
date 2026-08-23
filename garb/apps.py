from django.apps import AppConfig


class GarbConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "garb"
    verbose_name = "Django Garb"

    def ready(self):
        from garb.config import apply_admin_defaults

        apply_admin_defaults()
