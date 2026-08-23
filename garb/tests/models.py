from django.contrib import admin
from django.db import models


def test_app_label():
    return Blog._meta.app_label


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Blog(models.Model):
    name = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=160, blank=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="blogs",
    )
    published_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
        permissions = [('can_hire','Can hire comments')]




class BlogComment(models.Model):
    blog = models.ForeignKey(
        Blog,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class User(models.Model):
    """
    Class to test menu marking as active if two apps have model with same name
    """
    name = models.CharField(max_length=64)

class BlogAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name', 'category', 'deleted')
    list_display = ('name', 'subtitle', 'category', 'deleted')
    search_fields = ('name', 'subtitle')
    date_hierarchy = 'published_at'
    fieldsets = (
        (None, {'fields': ('name', 'subtitle', 'content', 'category', 'deleted')}),
        ('Publication', {'fields': ('published_at',)}),
    )


class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 1


BlogAdmin.inlines = (BlogCommentInline,)


admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment)
admin.site.register(Category)
admin.site.register(User)
