from django.urls import path

from travelapp import views

urlpatterns=[
    path('home',views.home,name='home')
]