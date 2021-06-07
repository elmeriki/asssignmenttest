from django.urls import path,include
from .import views

urlpatterns = [
path('', views.welcome, name='welcome'),
path('dashboard', views.dashboard, name='dashboard'),
path('insert', views.insert, name='insert'),
path('deleteform', views.deleteform, name='deleteform'),
path('deletequery', views.deletequery, name='deletequery'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),

]
