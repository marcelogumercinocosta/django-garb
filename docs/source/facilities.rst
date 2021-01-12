Facilities
=============

Grid templates
---------------


Grid template menu + 1 column.::

    {% block content %}
        <div id="content-main">
            -- column 1
        </div>
    {% endblock %}

.. image:: _static/facilities1.png
    :alt: Django Garb Facilities4


Grid template menu + 2 columns.::

    {% block content %}
        <div id="content-main" >
            <div class="change-columns">
                <div class="main-column">
                    -- column 1
                </div>
                <div class="box-column box-garb">
                    -- column 2
                </div>
        </div>
    {% endblock %}

.. image:: _static/facilities2.png
    :alt: Django Garb Facilities4


Turn off the menu
-----------------

Create template + button.::

    {% block content %}
        <div id="content-main">
            <div id='view_all>
            </div>
            <button type="button" class="button float-right"  data-name="view_all">
                <i class="fa fa-eye fa-lg p-1"></i>
            </button>
        </div>
    {% endblock %}

Add Js::

    {% block extrajs %}
        <script src="{% static 'js/garb_page_wide.js' %}"></script>
    {% endblock %}

Menu ON

.. image:: _static/facilities3.png
    :alt: Django Garb Facilities4

Menu OFF

.. image:: _static/facilities4.png
    :alt: Django Garb Facilities4

Set breadcrumbs
----------------

Add ViewContextMixin in view::

    from garb.views import ViewContextMixin

Use in class base view::

    class HelloView(ViewContextMixin, TemplateView):
        template_name = "hello_world.html"
        title = "hello world"

.. image:: _static/facilities5.png
    :alt: Django Garb Facilities4