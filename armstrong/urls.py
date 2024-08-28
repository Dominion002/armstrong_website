from django.urls import path
from . import views
urlpatterns = [  
    path("", views.index, name='home'),
    path("register", views.register, name='register'),
    path("login", views.loginPage, name='login'),
    path("logout", views.logoutPage, name='logout'),
    path("settings", views.settings, name='settings'),
    path("sendFeedback", views.send_feedback, name='sendFeedback'),
    path('check-armstrong/', views.check_armstrong, name='check_armstrong'),
     path('check_armstrongRange/', views.check_armstrongRange, name='check_armstrongRange'),
     path('history/', views.user_history, name='user_history'),
    ]

handler404 = ('armstrong.views.handling_404')