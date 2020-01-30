from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login, name='firstlogin'),
    path('trylogin', views.trylogin, name='tryLogin'),
    path('tryregister', views.tryregister, name='tryRegister'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout')
]