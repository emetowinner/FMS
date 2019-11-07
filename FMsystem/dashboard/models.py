from django.conf import settings
from django.db import models

User= settings.AUTH_USER_MODEL

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User,default=1, verbose_name="Users", on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=False,blank=False,)
    first_name = models.CharField(max_length=30 )
    last_name = models.CharField(max_length=30 )
    birth_date = models.DateField(default=20/7/1993)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=254)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    about_me = models.CharField(max_length=300)
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "UserProfile"
