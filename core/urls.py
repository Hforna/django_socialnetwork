"""
URL configuration for core project.

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
from django.urls import path, include
from instamain.urls import urlpatterns as home
from profiles.urls import urlpatterns as url_profiless
from accounts.urls import urlpatterns as url_accountss
from django.conf.urls.static import static
import core.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(home)),
    path("profile", include(url_profiless)),
    path("accounts", include(url_accountss)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

