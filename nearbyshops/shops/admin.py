# Register your models here.

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import Shop


@admin.register(Shop)
class ShopAdmin(GISModelAdmin):
    list_display = ("name", "location")
