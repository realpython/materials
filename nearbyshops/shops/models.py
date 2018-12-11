#from django.db import models
from django.contrib.gis.db import models

from django.contrib.gis.geos import  Point

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def save(self, **kwargs):
        super(Shop, self).save(**kwargs)
