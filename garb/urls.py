from django.urls import path
from django.views.i18n import JavaScriptCatalog

app_name = 'garb'

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='jsi18n'),
]
