from django.contrib import admin

from app3.models import Car,Contact

from app4.models import Booking

# Register your models here.
admin.site.register(Car)
admin.site.register(Booking)
admin.site.register(Contact)