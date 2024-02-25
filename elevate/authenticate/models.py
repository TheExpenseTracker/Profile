from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class authenticate(models.Model):
    item = models.CharField(max_length = 50 )
    price =  models.FloatField()

    def __str__(self) :
        return str(self.item)
    
class Customer(models.Model):
    user= models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=200, null=True)
    phone= models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)
    profile_pic=models.ImageField(default="profile.png",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    def __str__(self) :
        return str(self.name)
    
