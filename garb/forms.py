
from copy import deepcopy
from dataclasses import fields

from django import forms
from django.forms.fields import DateField
from django.forms.utils import ErrorDict, flatatt
from django.utils.safestring import mark_safe


def with_metaclass(meta, *bases):
    return meta(str("NewBase"), bases, {})


class Fieldset(object):
    def __init__(self, form, name, boundfields, legend='', classes='', description=''):
        self.form = form
        self.boundfields = boundfields
        self.classes = classes
        self.description = mark_safe(description)
        self.name = name

    def _errors(self):
        return ErrorDict(((k, v) for (k, v) in self.form.errors.iteritems() if k in [f.name for f in self.boundfields]))
    errors = property(_errors)

    def __iter__(self):
        for bf in self.boundfields:
            if isinstance(bf.field, forms.fields.DateField):
                if 'class' in bf.field.widget.attrs:
                    bf.field.widget.attrs['class'] += ' vDateField'
                else:
                    bf.field.widget.attrs.update({'class':'vDateField'})
            yield _mark_row_attrs(bf, self.form)

    def __repr__(self):
        return "%s('%s', %s, classes='%s', description='%s')" % ( self.__class__.__name__, self.name, [f.name for f in self.boundfields], self.classes, self.description)


class FieldsetCollection(object):
    def __init__(self, form, fieldsets):
        self.form = form
        self.fieldsets = fieldsets
        self._cached_fieldsets = []

    def __len__(self):
        return len(self.fieldsets) or 1

    def __iter__(self):
        if not self._cached_fieldsets:
            self._gather_fieldsets()
        for field in self._cached_fieldsets:
            yield field

    def __getitem__(self, key):
        if not self._cached_fieldsets:
            self._gather_fieldsets()
        for field in self._cached_fieldsets:
            if field.name == key:
                return field
        raise KeyError

    def _gather_fieldsets(self):
        if not self.fieldsets:
            self.fieldsets = (('', {'fields': self.form.fields.keys(), 'legend': ''}),)
        for name, options in self.fieldsets:
            try:
                field_names = [n for n in options['fields'] if n in self.form.fields]
            except KeyError:
                message = "Fieldset definition must include 'fields' option."
                raise ValueError(message)
            boundfields = [forms.forms.BoundField(self.form, self.form.fields[n], n) for n in field_names]
            self._cached_fieldsets.append(Fieldset(self.form, name, boundfields, options.get('legend', None), ' '.join(options.get('classes', (''))), options.get('description', '')))


def _get_meta_attr(attrs, attr, default):
    try:
        ret = getattr(attrs['Meta'], attr)
    except (KeyError, AttributeError):
        ret = default
    return ret


def _set_meta_attr(attrs, attr, value):
    try:
        setattr(attrs['Meta'], attr, value)
        return True
    except KeyError:
        return False


def get_fieldsets(bases, attrs):
    """Get the fieldsets definition from the inner Meta class."""
    fieldsets = _get_meta_attr(attrs, 'fieldsets', None)
    if fieldsets is None:
        #grab the fieldsets from the first base class that has them
        for base in bases:
            fieldsets = getattr(base, 'base_fieldsets', None)
            if fieldsets is not None:
                break
    fieldsets = fieldsets or []
    return fieldsets


def get_fields_from_fieldsets(fieldsets):
    """Get a list of all fields included in a fieldsets definition."""
    fields = []
    try:
        for name, options in fieldsets:
            fields.extend(options['fields'])
    except (TypeError, KeyError):
        raise ValueError('"fieldsets" must be an iterable of two-tuples, ' 'and the second tuple must be a dictionary ' 'with a "fields" key')
    return fields or None


def get_row_attrs(bases, attrs):
    """Get the row_attrs definition from the inner Meta class."""
    return _get_meta_attr(attrs, 'row_attrs', {})


def _mark_row_attrs(bf, form):
    row_attrs = deepcopy(form._row_attrs.get(bf.name, {}))
    if bf.field.required:
        req_class = 'required'
    else:
        req_class = 'optional'
    if bf.errors:
        req_class += ' error'
    if 'class' in row_attrs:
        row_attrs['class'] = row_attrs['class'] + ' ' + req_class
    else:
        row_attrs['class'] = req_class
    return bf


class GarbFormBaseMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['base_fieldsets'] = get_fieldsets(bases, attrs)
        fields = get_fields_from_fieldsets(attrs['base_fieldsets'])
        if (_get_meta_attr(attrs, 'fields', None) is None and
            _get_meta_attr(attrs, 'exclude', None) is None):
            _set_meta_attr(attrs, 'fields', fields)
        attrs['base_row_attrs'] = get_row_attrs(bases, attrs)

        new_class = super(GarbFormBaseMetaclass, cls).__new__(cls, name, bases, attrs)
        return new_class


class GarbFormMetaclass(GarbFormBaseMetaclass, forms.forms.DeclarativeFieldsMetaclass):
    pass


class GarbModelFormMetaclass(GarbFormBaseMetaclass, forms.models.ModelFormMetaclass):
    pass


class GarbBaseForm(object):
    def __init__(self, *args, **kwargs):
        self._fieldsets = deepcopy(self.base_fieldsets)
        self._row_attrs = deepcopy(self.base_row_attrs)
        self._fieldset_collection = None
        super(GarbBaseForm, self).__init__(*args, **kwargs)

    @property
    def fieldsets(self):
        if not self._fieldset_collection:
            self._fieldset_collection = FieldsetCollection( self, self._fieldsets)
        return self._fieldset_collection

    def __iter__(self):
        for bf in super(GarbBaseForm, self).__iter__():
            yield _mark_row_attrs(bf, self)

    def __getitem__(self, name):
        bf = super(GarbBaseForm, self).__getitem__(name)
        return _mark_row_attrs(bf, self)


class GarbForm(with_metaclass(GarbFormMetaclass, GarbBaseForm), forms.Form):
    __doc__ = GarbBaseForm.__doc__


class GarbModelForm(with_metaclass(GarbModelFormMetaclass, GarbBaseForm), forms.ModelForm):
    __doc__ = GarbBaseForm.__doc__


class BasePreviewFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(BasePreviewFormMixin, self).__init__(*args, **kwargs)
        self.preview = self.check_preview(kwargs.get('data', None))

    def check_preview(self, data):
        if data and data.get('submit', '').lower() == u'preview':
            return True
        return False

    def is_valid(self, *args, **kwargs):
        if self.preview:
            return False
        return super(BasePreviewFormMixin, self).is_valid()


class PreviewModelForm(BasePreviewFormMixin, GarbModelForm):
    pass


class PreviewForm(BasePreviewFormMixin, GarbForm):
    pass