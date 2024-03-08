from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"), 
    path('about',views.about,name="about"),
    path('cameras',views.cameras,name="cameras"),
    path('contact',views.contact,name="contact") ,
    path('add',views.add,name="add"),
    path('edit/<id>/',views.edit,name="edit"),
    path('delete/<id>/', views.delete, name="delete"),
    path('cameras/details/<id>',views.detailed,name="detailed"),
    path('service',views.service,name="service"),
    path('clientreviews',views.client,name="client")
  
   
]