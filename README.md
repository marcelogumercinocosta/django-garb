
<h1 align="center"> Django Garb </h1>

<h3 align="center">Modern theme for Django admin interface</h3>

<h2 align="center">
  <img src="https://repository-images.githubusercontent.com/254154082/4cd40780-b23b-11ea-9642-82d6d011cc63" float="center"/>
</h2>


## About 
Django Garb is alternative theme/skin/extension for [Django](http://www.djangoproject.com>) administration interface.

## Compatibility

Django Garb 2026.8 supports Python 3.10+ and Django 5.1, 5.2 LTS, and 6.0.
Django 6.0 itself requires Python 3.12+. Install the package with:

```console
python -m pip install django-garb
```

Add `garb` before `django.contrib.admin` so Django finds the themed templates
first:

```python
INSTALLED_APPS = [
    "garb",
    "django.contrib.admin",
]
```

For deployment, run `python manage.py collectstatic` after upgrading.

This release drops support for Django versions older than 5.1 and Python
versions older than 3.10. Projects that still need the legacy stack must pin the
previous Django Garb release.

## Front-end development

The Bootstrap, bootstrap-select, jQuery, Toast, and Pace files are distributed
locally. Reproduce them and compile the theme with:

```console
npm ci
npm run vendor:sync
npm run build:css
```

See [docs/VENDORS.md](docs/VENDORS.md) for exact versions, licenses, sources,
checksums, and the jQuery 4 compatibility decision. Visual regression usage is
documented in [tests/visual/README.md](tests/visual/README.md).

## Docs
**Installation + Configuration** <br>
Documentation: [https://django-garb.readthedocs.io/en/latest/](https://django-garb.readthedocs.io/en/latest/)

## Screenshots
Screenshots: [https://django-garb.readthedocs.io/en/latest/screenshots.html](https://django-garb.readthedocs.io/en/latest/screenshots.html)

## License 📝
This project is under MIT [LICENSE](https://github.com/marcelogumercinocosta/django-garb/tree/master/LICENSE)
