from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import *
from app3.models import Car


# Create your views he
# re.
def index(request):
    return render(request, 'index1.html')

def about(request):
    return render(request, 'about1.html')

def services(request):
    return render(request, 'services1.html')

def cars(request):
    c = Car.objects.all()
    return render(request, 'cars1.html', {'c': c})

def contact(request):
    return render(request, 'contact1.html')

def dealer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/cardealer')
        else:
            messages.error(request,"Bad Credentials")
            return render(request, 'login1.html', {'username': username, 'password': password})
    return render(request, 'login1.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('/cardealer/login')
    return render(request, 'registration1.html')

def Logout(request):
    logout(request)
    return redirect('/')

def managebooking(request):
    user = request.user
    j = Car.objects.filter(user=user)
    al = []
    for i in j:
        a = Booking.objects.filter(car_name = i.id)
        # print(a)
        al.append(a)
    print(al)
    return render(request,'showbookings.html',{'s':al})

def app_approve(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Approve'
    a.save()
    return redirect('/dealerdash/showbooking/')

def app_reject(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Pending'
    a.save()
    return redirect('/dealerdash/showbooking/')
# Create your views here.

