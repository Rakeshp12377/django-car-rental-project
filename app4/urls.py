from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('services/',views.services),
    path('cars/',views.cars),
    path('contact/',views.contact),
    path('login/',views.dealer_login),
    path('registration/',views.registration),
    path('logout/',views.Logout),
    ]