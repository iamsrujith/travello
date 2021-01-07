from django.urls import path
from accounts import views

urlpatterns=[
    # path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout')
]