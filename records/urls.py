from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_patients, name='search'),
    path('search1/', views.search_patients1, name='search1'),
    path('dashboard/', views.dashboard, name='dashboard'),
]