from django import forms,  template, views, urls
from django.template.loader import render_to_string
from django.template import loader
from garb.forms import GarbForm, GarbModelForm

register = template.Library()



def select_template_from_string(arg):
    """
    Select a template from a string, which can include multiple
    template paths separated by commas.
    """
    if ',' in arg:
        tpl = loader.select_template( [tn.strip() for tn in arg.split(',')])
    else:
        tpl = loader.get_template(arg)
    return tpl

@register.filter
def render(form, template_name=None):
    default = 'garb/form/garb_form.html'
    tpl = select_template_from_string(template_name or default)
    return tpl.render({'form': form})

@register.filter
def value_text(boundfield):
    val = boundfield.value()
    return str( dict(getattr(boundfield.field, "choices", [])).get(val, val))


@register.filter
def selected_values(boundfield):
    val = boundfield.value()
    choice_dict = dict(getattr(boundfield.field, "choices", []))
    return [str(choice_dict.get(v, v)) for v in val]


@register.filter
def optional(boundfield):
    return not boundfield.field.required


@register.filter
def is_checkbox(boundfield):
    return isinstance(boundfield.field.widget, forms.CheckboxInput)


@register.filter
def is_multiple(boundfield):
    return isinstance(boundfield.field, forms.MultipleChoiceField)


@register.filter
def is_select(boundfield):
    return isinstance(boundfield.field, forms.ChoiceField)


@register.filter
def is_radio(boundfield):
    return 'radio' in boundfield.field.widget.__class__.__name__.lower()


@register.filter
def label(boundfield, contents=None):
    """Render label tag for a boundfield, optionally with given contents."""
    label_text = contents or boundfield.label
    id_ = boundfield.field.widget.attrs.get('id') or boundfield.auto_id
    return render_to_string("garb/form/label.html", { "label_text": label_text, "id": id_, "field": boundfield})
