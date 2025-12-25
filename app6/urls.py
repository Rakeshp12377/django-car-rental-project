from django.urls import path
from . import views

urlpatterns = [
  path('',views.index3),
  # path('addcar/',views.addcar),
  path('table1/',views.table1),
 ]