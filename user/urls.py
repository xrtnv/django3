from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .apps import UserConfig
from .views import UserRegisterView, PasswordResetView, email_confirm

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_confirm, name='email_confirm'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
]
