from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('browse', views.browse, name='browse'),
    path('write', views.write, name='write'),
    path('submit', views.submit, name='submit'),
    path('search', views.search, name='search'),
    path('read/<int:id_number>', views.read, name='read'),
    path('extend/<int:id_number>', views.extend, name='extend'),
    path('add', views.add, name='add'),
    path('mystories', views.mystories, name='mystories'),
    path('change', views.change, name='change'),
]