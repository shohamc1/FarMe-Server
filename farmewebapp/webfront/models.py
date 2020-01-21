from django.db import models

# Create your models here.

class data (models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    device_id = models.IntegerField (default=0)
    latitude = models.DecimalField (default=0, max_digits=7, decimal_places=5)
    longitude = models.DecimalField (default=0, max_digits=7, decimal_places=5)
    amb_ll = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    temp = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    loc_humidity = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm1 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm2 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm3 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm4 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm5 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm6 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm7 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    sm8 = models.DecimalField (default=0, max_digits=10, decimal_places=5)
    timestamp = models.DateTimeField(default='2000-01-01 12:00:00')