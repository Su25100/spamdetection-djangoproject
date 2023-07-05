"""
URL configuration for Apiproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from spamapp import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spamcheck/',views.PhoneNumberListAPIView.as_view()),
    path('srchbyno/<str:phone_no>/',views.SearchByNoAPIView.as_view()),
    path('markspam/',views.MarkNoAsSpamAPIView.as_view()),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('api/verifytoken',TokenVerifyView.as_view())
]
