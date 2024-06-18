from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "content", "created_at", "is_published", "views_count")
    search_fields = ("title", "content")
