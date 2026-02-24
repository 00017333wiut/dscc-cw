from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "published", "created_at")
    list_filter = ("published", "created_at", "category")
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)


admin.site.register(Category)
admin.site.register(Tag)
