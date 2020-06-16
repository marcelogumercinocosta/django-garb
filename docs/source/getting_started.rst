Getting Started
===============

Installation
------------


1. You can get stable version of Django Suit by using pip or easy_install::

    pip install git+https://github.com/marcelogumercinocosta/django-garb.git

2. You will need to add the ``'garb'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file.::

    INSTALLED_APPS = (
        ...
        'garb',
        'django.contrib.admin',
    )

.. important:: ``'garb'`` must be added before ``'django.contrib.admin'`` and if you are using third-party apps.

Deployment
----------

Deployment with Django Garb should not be different than any other Django application. If you have problems with deployment on production, read `Django docs on wsgi <https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/>`_ first.

.. note:: If you deploy your project with Apache or ``Debug=False`` don't forget to run ``./manage.py collectstatic``

