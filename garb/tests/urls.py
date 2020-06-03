from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='blog1'),
    path('', TemplateView.as_view(template_name='base.html'), name='blog2'),
    path('', TemplateView.as_view(template_name='base.html'), name='blog3'),
    path('admin/', admin.site.urls),
]