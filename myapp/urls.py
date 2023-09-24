from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('hello',views.hello_worls),
    path('',views.homePage),
    path('url/task' or 'url',views.taskPage),
    path('task',views.taskPage),
] 
