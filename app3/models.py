from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField


# Create your dels here.

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    pardprice = models.IntegerField()
    parhprice = models.IntegerField()
    company= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    car_img = models.ImageField(upload_to='car')
    is_published = models.BooleanField(default=False)
    text= models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    massage= models.TextField()
    
