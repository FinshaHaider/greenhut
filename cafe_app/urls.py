# from django.contrib import admin
from django.urls import include, path

from .import views

app_name="cafe_app"

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu',views.menu,name='menu'),
    path('menu/addmenu',views.addmenu,name='addmenu'),
    path('updatemenu/<pkey>',views.updatemenu,name='updatemenu'),
    path('deletemenu/<pkey>',views.deletemenu,name='deletemenu'),
    
    
   ] 