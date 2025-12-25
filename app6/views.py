from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

from app3.models import Car

from app4.models import Booking


def index3(request):
    a2 = Booking.objects.filter(user=request.user.id).count()
    a1 = Booking.objects.filter(user=request.user.id,is_status='Pending').count()
    cotext={
        'b':a2,
        'b1':a1
    }
    return render(request, 'index3.html',cotext)

def table1(request):
    c = Booking.objects.filter(user=request.user)
    return render(request, 'table1.html',{'c':c})