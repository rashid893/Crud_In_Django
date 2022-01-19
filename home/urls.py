from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
path('',views.index,name="home"),
path('home/',views.home,name="home"),
path('show/',views.show,name="show"),
path('send/',views.send,name="send"),
path('delete/',views.delete,name="delete"),
path('edit/',views.edit,name="edit"),
path('recordEdited/',views.recordEdited,name='recordEdited'),
]
