# from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

# hardcoded user location
# get user's location from IP:
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/geoip/
# or get user's location from HTML:
# https://www.w3schools.com/html/html5_geolocation.asp
latitude = 39.290_440
longitude = -76.612_330

user_location = Point(longitude, latitude, srid=4326)


# Create your views here.
class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "shops/index.html"
