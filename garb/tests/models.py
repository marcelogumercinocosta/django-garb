from django.db import models
from django.contrib import admin


def test_app_label():
    return Blog._meta.app_label


class Blog(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        permissions = [('can_hire','Can hire comments')]




class BlogComment(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class User(models.Model):
    """
    Class to test menu marking as active if two apps have model with same name
    """
    name = models.CharField(max_length=64)

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name',)
    list_display = ('id', 'name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(User)
