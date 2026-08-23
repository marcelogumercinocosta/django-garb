# Verification results

Verified on 2026-08-20.

## Django and Python

All 12 supported combinations completed `django check` and 33 tests with
`DeprecationWarning` promoted to errors:

- Django 5.1 on Python 3.10, 3.11, 3.12, and 3.13;
- Django 5.2 on Python 3.10, 3.11, 3.12, 3.13, and 3.14;
- Django 6.0 on Python 3.12, 3.13, and 3.14.

Migration drift check reported no changes.

## Browser and visual

The browser suite validated HTML and 10 screenshots at `1680x984`, covering
index, list, change, delete, history, login, and every public theme. A second
run matched all approved baselines within the 1% tolerance. Dropdowns, sidebar
collapse, bootstrap-select, dynamically added selects, Toast, and Pace passed
without failed local assets or uncaught JavaScript errors.

The resulting shell, cards, table hierarchy, sidebar, and two-column change
form were reviewed against `docs/source/_static/`. No redesign was introduced.

## Build and installation

SCSS compiled without warnings. Wheel and sdist `2026.8.0` passed `twine
check`. A clean Python 3.12/Django 6.0 container installed the wheel and found
the admin templates, compiled translation, CSS, source maps, JavaScript, and
all seven representative vendor assets through Django's loaders.

`openspec validate support-django-5-and-modernize-vendors --strict` passed.
