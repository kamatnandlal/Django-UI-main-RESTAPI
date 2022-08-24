from django.urls import path 
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('add',views.add, name="add"),
   path('postadd',views.postadd, name="postadd"),
   path('delete',views.delete, name="delete"),
   path('update',views.update, name="update"),
   path('postupdate',views.postupdate, name="postupdate")
   ]