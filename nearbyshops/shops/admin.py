#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin, OSMGeoAdmin
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance

from .models import Shop

user_location = fromstr('POINT(-9.544372557268286 30.35495327369988)', srid=4326)
 
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display= ('name','location')

    def dist(self, obj):
        d = obj.location.distance(user_location)
        return d
    dist.short_description = 'Distance'




