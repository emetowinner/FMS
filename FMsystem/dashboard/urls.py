from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('map/', views.map, name='map'),
    path('notification/', views.notification, name='notification'),
    path('profile/', views.user, name='profile'),
    path('graph/',views.graph,name='graph')
]