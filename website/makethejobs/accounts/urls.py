from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('change-password/', views.ChangePassword.as_view(), name='change_password'),
    path('reset-password/', views.ResetPassword.as_view(), name='reset_password'),
    path('forgotten-password/', views.ForgottenPassword.as_view(), name='forgotten_password'),
]