"""conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from ca import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_auth.views import LoginView, LogoutView
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/register/", RegistrationView.as_view(success_url='/dashboard/'), name="django_registration_register"),
    
    path("accounts/",include("django_registration.backends.one_step.urls")),
    
    path("accounts/",include("django.contrib.auth.urls")),
    
    #  path('login/', LoginView.as_view(template_name='account/login.html'), name='login',),
    path('logged-in/',views.dashboardview,name='logged_in',),
    # path('logout/',LogoutView.as_view(),name='logout',),
    
    path("api/", include("ca.api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/rest-auth/", include("rest_auth.urls")),
    url(r'rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', views.index, name='index'),
    path('dashboard', views.index, name='index')
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)