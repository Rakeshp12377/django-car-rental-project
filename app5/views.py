from django.shortcuts import render,redirect

from app3.models import Car

from app4.models import Booking


# Create your views here.
def index2(request):
    b2 =0
    j = Car.objects.filter(user=request.user.id)
    for i in j:
        bb = Booking.objects.filter(car_name=i.id).count()
        b2 += bb
    b1 = Car.objects.filter(user=request.user.id).count()
    b3 = Booking.objects.filter(user=request.user.id,is_status='Pending').count()
    context={
        'b':b2,
        'b1':b1,
        'b3':b3
    }
    return render(request, 'index2.html',context)

def addcar(request):
    if request.method == "POST":
        cname= request.POST['cname']
        cimg= request.FILES['car_image']
        company= request.POST['company']
        price1= request.POST['price1']
        price2 = request.POST['price2']
        location= request.POST['location']
        is_published= request.POST['is_published']

        c = Car.objects.create(user=request.user,car_name=cname,car_img=cimg,company=company,pardprice=price1,parhprice=price2,location=location,is_published=is_published)

        return redirect('/dashboard/table')
    return render(request, 'addcar.html')

def table(request):
    c = Car.objects.filter(user=request.user).order_by("-id")
    return render(request, 'table.html',{'c':c})

def atable(request):
    user = request.user
    cars = Car.objects.filter(user=user)
    bookings = Booking.objects.filter(car_name__in=cars)
    return render(request, 'atable.html', {'s': bookings})

def app_approve(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Approve'
    a.save()
    return redirect('/dashboard/atable/')

def app_reject(request,id):
    a = Booking.objects.get(id=id)
    a.is_status = 'Pending'
    a.save()
    return redirect('/dashboard/atable/')

def editcar(request,id):
    car = Car.objects.get(id=id)
    if request.method == "POST":
        cname= request.POST['cname']
        cimg= request.FILES.get('car_image')
        company= request.POST['company']
        price1= request.POST['price1']
        price2 = request.POST['price2']
        location= request.POST['location']
        is_published= request.POST['is_published']

        car.car_name = cname
        if cimg:
            car.car_img = cimg
        car.user = request.user
        car.company = company
        car.pardprice = price1
        car.parhprice = price2
        car.location = location
        car.is_published = is_published

        car.save()

        return redirect('/dashboard/table')
    return render(request,'editcar.html',{'car':car})

def deletecar(request,id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('/dashboard/table')

