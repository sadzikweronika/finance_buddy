from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),  # Nowy endpoint
    path('profile/', ProfileView.as_view(), name='profile'),  # Endpoint profilu
]