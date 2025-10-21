from core.models import Blog
from django.contrib import admin


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
