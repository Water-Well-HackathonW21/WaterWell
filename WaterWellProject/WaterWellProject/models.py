from django.contrib.gis.db import models

class WaterWell(models.Model):
    location = models.PointField()
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100) 
    description = models.CharField(max_length=200)
