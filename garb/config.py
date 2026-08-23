from django.conf import settings
from django.contrib.admin import ModelAdmin


def default_config():
    return {
        # configurable
        'PROJECT_NAME': 'Django Garb',
        'LIST_PER_PAGE': 15,
        'MENU': [],
        'ADMIN_ACTIONS_ALL': True,
        'ADMIN_WIDGET_CAN': True,
        'MENU_ONLY_AUTH': False,
        'ROUTE_PROFILE': False,
        'NAME_PROFILE': '',
        'THEME': 'default',
    }


def get_config(param=None):
    configured = getattr(settings, "GARB_CONFIG", {}) or {}
    config = {**default_config(), **configured}
    if param:
        value = config.get(param)
        return default_config().get(param) if value is None else value
    return config


def apply_admin_defaults():
    """Apply Garb's documented defaults while allowing subclass overrides."""
    ModelAdmin.actions_on_top = False
    ModelAdmin.actions_on_bottom = True
    ModelAdmin.list_per_page = get_config("LIST_PER_PAGE")
