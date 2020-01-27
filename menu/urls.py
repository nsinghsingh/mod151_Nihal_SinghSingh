from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('browse', views.browse, name='browse'),
    path('write', views.write, name='write'),
]