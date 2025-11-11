# flake8: noqa
from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Post model.

    Provides customization options for how Post objects are displayed
    and managed in the Django admin interface.

    Attributes:
        list_display (tuple): Fields shown in the admin list view,
        including ID, title, user, visibility, and creation date.

        list_filter (tuple): Filters available in the sidebar for
        narrowing down posts by visibility or creation date.

        search_fields (tuple): Fields that can be searched using
        the admin search bar, such as title and content.
    """

    list_display = ("id", "title", "user", "is_public", "created_at")
    list_filter = ("is_public", "created_at")
    search_fields = ("title", "content")

    class Media:
        css = {"all": ("css/admin_ckeditor.css",)}
