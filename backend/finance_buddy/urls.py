"""
URL configuration for finance_buddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import example_api, login, finances, dashboard, expense_detail, user_profile, ExpenseListCreateAPIView, ExpenseDetailAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/example_api/', example_api, name='example_api'),
    path('login/', login, name='login'),
    path('finances/', finances, name='finances'),
    path('dashboard/', dashboard, name='dashboard'),
    path('expense/<uuid:expense_id>/', expense_detail, name='expense_detail'),
    path('user/<uuid:user_id>/', user_profile, name='user_profile'),
    path('api/expenses/', ExpenseListCreateAPIView.as_view(), name='expense-list'),
    path('api/expenses/<int:pk>/', ExpenseDetailAPIView.as_view(), name='expense-detail'),
]
