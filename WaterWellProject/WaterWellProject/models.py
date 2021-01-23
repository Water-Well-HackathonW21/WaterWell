from django.contrib.gis.db import models

class WaterWell(models.Model):
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    #icon = 
    description = models.CharField(max_length=100)
