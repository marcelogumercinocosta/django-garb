Getting Started
===============

Installation
------------


1. Install Django Garb with pip (Python 3.10+ and Django 5.1 through 6.0)::

    python -m pip install django-garb

2. You will need to add the ``'garb'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file.::

    INSTALLED_APPS = (
        ...
        'garb',
        'django.contrib.admin',
    )

.. important:: ``'garb'`` must be added before ``'django.contrib.admin'`` and other apps that override the same admin templates.

Supported versions
------------------

* Django 5.1: Python 3.10 through 3.13
* Django 5.2 LTS: Python 3.10 through 3.14
* Django 6.0: Python 3.12 through 3.14

The 2026.8 release intentionally drops older Django and Python versions. Keep
the preceding Django Garb release pinned when an application cannot yet move to
this matrix.

Deployment
----------

Deployment with Django Garb should not be different than any other Django application. If you have problems with deployment on production, read `Django docs on wsgi <https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/>`_ first.

.. note:: If you deploy your project with Apache or ``Debug=False`` don't forget to run ``./manage.py collectstatic``

After every Django Garb upgrade, run::

    python manage.py collectstatic --noinput

Front-end build
---------------

Published Python packages already contain compiled CSS and local vendor assets.
Maintainers can reproduce them from exact versions in ``package-lock.json``::

    npm ci
    npm run vendor:sync
    npm run build:css

The vendor inventory and checksums are in ``docs/VENDORS.md``. Browser and
visual-regression instructions are in ``tests/visual/README.md``.
