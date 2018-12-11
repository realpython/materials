from rest_framework import generics
from rest_framework_gis.pagination import GeoJsonPagination
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry

from django.views.generic.base import View
from django.shortcuts import render
from .models import *
from django.views import generic

longitude  = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)
 
class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6] 
    template_name = 'shops/index.html' 

home = Home.as_view()
