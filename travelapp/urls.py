
from . import views
from django.urls import path
#from django.contrib import settings
#from django.conf.urls.static  import static

urlpatterns = [
path('', views.demo,name='demo'),
path('', views.demo2,name='demo2'),
path('',views.new,name='new'),
path('add/', views.tem,name='tem'),

#path('add/',views.addition,name='addition'),
]



