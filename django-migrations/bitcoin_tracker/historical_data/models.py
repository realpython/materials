from django.db import models


class PriceHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    volume = models.DecimalField(max_digits=7, decimal_places=3)
