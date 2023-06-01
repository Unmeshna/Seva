from django.urls import path
from . import views

urlpatterns = [

     path('',views.index, name='index'),

    path('index',views.index, name='index'),
    path('user_signup',views.user_signup, name='user_signup'),
     path('user_login',views.user_login, name='user_login'),
    path('register', views.register, name='register'),
     path('logout', views.logout, name='logout'),
    #path('professional_signup', views.professional_signup, name='professional_signup')
]