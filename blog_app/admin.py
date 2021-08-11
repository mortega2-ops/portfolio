from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Blog


class BlogModelAdmin(MarkdownxModelAdmin):
    list_display = ["title", "updated", "date"]
    list_filter = ["updated", "date"]
    search_fields = ["title", "content"]


admin.site.register(Blog, BlogModelAdmin)



