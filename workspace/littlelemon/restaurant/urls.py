# from django.contrib import admin 
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    # message means the view is protected due to needing authenication
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),


]