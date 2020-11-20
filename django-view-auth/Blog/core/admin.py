from django.contrib import admin
from core.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
