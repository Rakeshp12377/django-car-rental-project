from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('services/',views.services),
    path('cars/',views.cars),
    path('contact/',views.contact),
    path('logout/',views.Logout),
    path('single_car/<int:id>/',views.single_car),
    path('booking/<int:id>/', views.booking),
    path('login1/',views.user_login),
    path('registration1/',views.registration1),
]
