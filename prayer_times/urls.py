
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search-city/', views.search_city, name='search_city'),
    path('get-times/', views.get_prayer_times, name='get_times'),
]