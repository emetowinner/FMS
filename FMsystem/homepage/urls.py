from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout')
]