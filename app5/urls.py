from django.urls import path
from . import views

urlpatterns = [
 path('',views.index2),
 path('addcar/',views.addcar),
 path('table/',views.table),
 path('atable/',views.atable),
 path('app_approve/<int:id>/',views.app_approve),
 path('app_reject/<int:id>/',views.app_reject),
 path('editcar/<int:id>/',views.editcar),
 path('deletecar/<int:id>/',views.deletecar),
]