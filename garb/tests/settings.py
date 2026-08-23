# Django settings for testproject project.

import django
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = True

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('GARB_TEST_DATABASE', ':memory:'),
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
SECRET_KEY = '@x6=fyyw@s*24!$7uxz%#zm#+t5f811em$tyrv9s$9pz!j4*le'
ALLOWED_HOSTS = ['testserver', '127.0.0.1', 'localhost']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'garb.tests.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'garb',
    'garb.tests',
    'garb.tests.templatetags',
    'django.contrib.admin',
)

STATIC_URL = '/static/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tests/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

GARB_CONFIG = {
    'PROJECT_NAME': 'GARB BLOG',
    'THEME': os.environ.get('GARB_TEST_THEME', 'default'),
    'MENU': [
        {'label': 'Home', 'icon': 'fa-home', 'route': 'admin:index', 'auth': 'yes'},
        {
            'label': 'Content',
            'icon': 'fa-newspaper',
            'sub_itens': [
                {'model': 'tests.blog'},
                {'model': 'tests.category'},
                {'model': 'tests.blogcomment'},
            ],
        },
        {
            'label': 'Authentication and Authorization',
            'icon': 'fa-users',
            'sub_itens': [
                {'model': 'auth.user'},
                {'model': 'auth.group'},
            ],
        },
    ],
}
