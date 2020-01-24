from django.db import models

# Create your models here.

class var_data (models.Model):
    id = models.IntegerField (primary_key=True, default=0)
    device_id = models.IntegerField (default=0)
    latitude = models.DecimalField (default=0, max_digits=7, decimal_places=5)
    longitude = models.DecimalField (default=0, max_digits=7, decimal_places=5)