from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

from app3.models import Car

from app4.models import Booking

from app3.models import Contact


# Create your views he
# re.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def cars(request):
    c = Car.objects.all()
    return render(request, 'cars.html',{'c':c})

def contact(request):
    if request.method == 'POST':
      name= request.POST['name']
      email= request.POST['email']
      phone = request.POST['phone']
      massage = request.POST['massage']

      c = Contact.objects.create(name= name,email= email,phone=phone,massage=massage)

    return render(request,'contact.html')

def single_car(request,id):
    cd = Car.objects.get(id=id)
    return render(request, 'single_car.html',{'cd':cd})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,"Bad Credentials")
            return render(request, 'login.html', {'username': username, 'password': password})
    return render(request, 'login.html')

def registration1(request):
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

        return redirect('/login1')
    return render(request, 'registration.html')

def Logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login1')
def booking(request,id):
    c = Car.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        # car_name = request.POST.get('car_name')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        plocation = request.POST['plocation']
        pdate = request.POST['pdate']
        ddate = request.POST['ddate']
        b = Booking.objects.create(user=user,car_name=c,plocation=plocation,pdate=pdate,ddate=ddate,name=name,email=email,phone=phone,is_booked=True)

        # return HttpResponse('Book Success.')
        return redirect('/')
    return render(request,'booking.html',{'c':c})
