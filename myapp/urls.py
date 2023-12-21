from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('adminlogin/', views.adninlogin, name='adminlogin'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('logout/', views.logout_view, name='logout'),
    path('login/',views.login,name='login'),
    path('admnhm/',views.admin_view,name='admin_home'),
]
