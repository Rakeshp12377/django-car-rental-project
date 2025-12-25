from django.db import models
from django.contrib.auth.models import User

from app3.models import Car

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car_name = models.ForeignKey(Car,on_delete=models.CASCADE)
    plocation = models.CharField(max_length=100)
    pdate = models.DateField()
    ddate = models.DateField()
    is_status = models.CharField(max_length=20,default='pending')
    is_booked = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
