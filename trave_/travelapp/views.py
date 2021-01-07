from django.http import HttpResponse
from django.shortcuts import render
from .models import place,blog
from django.contrib.auth.models import User,auth
from accounts import views

def home(request):
    obj=place.objects.all()
    obj1=blog.objects.all()

    return render(request,'index.html',{'results':obj,'results1':obj1})

