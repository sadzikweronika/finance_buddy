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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import example_api, login, finances, dashboard, expense_detail, user_profile, ExpenseListCreateAPIView, ExpenseDetailAPIView
from finance_buddy import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



schema_view = get_schema_view(
    openapi.Info(
        title="Finance Buddy API",
        default_version='v1',
        description="Dokumentacja API dla Finance Buddy",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@financebuddy.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/auth/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
