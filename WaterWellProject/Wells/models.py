from django.db import models

class Well(models.Model):
    status = models.CharField(max_length=20)
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.CharField(max_length=100)
# Create your models here.

# class Subscribe(models.Model):
#     email = models.EmailField(max_length = 200, null = False, blank = False)
#     country = models.CharField(max_length = 200, null = True, blank = True)
#     city = models.CharField(max_length = 200, null = True, blank = True)
#     store = models.CharField(max_length = 200, null = True, blank = True)
#     active = models.BooleanField(default=True)

#     class Meta: 
#         db_table = "subscribedb"
