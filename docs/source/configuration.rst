Configuration
=============

Templates
---------

You must extend ``base_site.html`` template to customize footer links, copyright text or to add extra JS/CSS files. Example file is available on `github <https://github.com/marcelogumercinocosta/django-garb/blob/develop/garb/templates/base.html>`_.

In the same way you can override any of Django Suit admin templates. More about customizing project's templates, you can read in `Django Admin Tutorial <https://docs.djangoproject.com/en/3.0/intro/tutorial02/#customizing-your-project-s-templates>`_

Customization
-------------

You can customize Django Garb behaviour by adding ``GARB_CONFIG`` configuration variable to your Django project ``settings.py`` file.

Configuration sample you can use as a start::

  # Django Suit configuration example
  GARB_CONFIG = {
    'PROJECT_NAME': 'GARB BLOG',
    'ADMIN_ACTIONS_ALL': True,
    'ADMIN_WIDGET_CAN': True,
    'THEME': 'hybrid',
    'MENU_ONLY_AUTH': False,
    'LIST_PER_PAGE': 15,
    'ROUTE_PROFILE': False,
    'MENU': [
        {'label': 'Home', 'icon': 'fa-home', 'route': 'admin:index', 'auth':'yes'},
        {'label': 'Authentication and Authorization', 'icon': 'fa-users', 'sub_itens': [
            {'model': 'auth.user'},
            {'model': 'auth.group'},
        ]},
        {'label': 'Website', 'icon': 'fa-globe-americas', 'sub_itens': [
            {'model': 'website.post'},
            {'model': 'website.contact'},
        ]},
        {'label': 'External', 'icon': 'fa-chart-line', 'sub_itens': [
            {'model': 'monitoramento.post'},
        ]},
    ],
  }


PROJECT_NAME
^^^^^^^^^^^^

Admin name that will appear in header <title> tags::

  GARB_CONFIG = {
      'PROJECT_NAME': 'GARB BLOG'
  }


ADMIN_ACTIONS_ALL
^^^^^^^^^^^^^^^^^

This parameter hides actions from the application list, even if the user has django admin permissions.::

  GARB_CONFIG = {
      'ADMIN_ACTIONS_ALL': False  # Default True
  }

ADMIN_WIDGET_CAN
^^^^^^^^^^^^^^^^

This parameter hides widgets add /remove /edit in the model list (select) in the forms admin::

  GARB_CONFIG = {
      'ADMIN_WIDGET_CAN': False  # Default True
  }

THEME
^^^^^

Select the theme for the admin::

  GARB_CONFIG = {
      'THEME': 'default' # 'hybrid','dark','light','alive'
  }
  

MENU_ONLY_AUTH
^^^^^^^^^^^^^^

The menu is visible only when authenticated::

  GARB_CONFIG = {
      'MENU_ONLY_AUTH': True # Default False
  }

LIST_PER_PAGE
^^^^^^^^^^^^^

Set change_list view ``list_per_page`` parameter globally for whole admin. You can still override this parameter in any ModelAdmin class::

  GARB_CONFIG = {
      'LIST_PER_PAGE': 20
  }

ROUTE_PROFILE AMD NAME_PROFILE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Activates link to the profile user's logged in form and defines which Naming access URL::

  GARB_CONFIG = {
      'ROUTE_PROFILE': "admin:colaborador_perfil"  #  Default 'False'
      'NAME_PROFILE': "PERFIL",
  }

MENU
^^^^

Most powerful of menu parameters - one parameter to rule them all :) You can rename, reorder, cross link, exclude apps and models, and even define custom menu items and child links.

The menu is completely manual and therefore editable

Here is full example of ``MENU`` from simple existing app reorder to defining custom menu items:


* **label:** Custom nane 
* **icon:** Only the first level of the menu has icons (https://fontawesome.com)
* **auth:** viewing permissions item  # default is ``no``

  * ``yes`` only logged in appears in the menu
  *  ``no`` only without logged in appears
  *  ``all`` appears in logged in and logged out
* **route**: Named url like ``admin:index``
* **sub_itens**: add sub-menus 
* **model**: set list for ``App.Model``
* **link**: set link other sites
* **permission**: shows if the user has permission
* **target**: reference the target of the <a> tag

Django Suit configuration example::

  GARB_CONFIG = {
    'MENU': [
      {'label': 'Home', 'icon': 'fa-home', 'route': 'admin:index', 'auth':'yes'},
      {'label': 'Authentication and Authorization', 'icon': 'fa-users', 'sub_itens': [
        {'model': 'auth.user'},
        {'model': 'auth.group'}
      ]},
      {'label': 'Website', 'icon': 'fa-globe-americas', 'sub_itens': [
        {'model': 'website.post'},
        {'model': 'website.contact'}
      ]},
      {'label': 'External', 'icon': 'fa-chart-line', 'sub_itens': [
        { 'label': 'sub1', 'link': 'www.uol.com.br', 'target':'_blank' },
      ]}
    ],
  }