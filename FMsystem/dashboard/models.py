from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30 )
    age = models.CharField(max_length=10)
    address = models.CharField(max_length=254)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    about_me = models.CharField(max_length=300)
# class FuelTrack(models.Model):
#     user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
#     unit_price = models.IntegerField(default = 145)
#     litter = models.IntegerField(default = 1)
#     vendor = models.CharField(max_length = 100)
