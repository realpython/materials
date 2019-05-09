from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ("name", "location")
