from django.contrib import admin

from .models import MarkdownContent


class MarkdownContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(MarkdownContent, MarkdownContentAdmin)
