"""home_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from rest_framework import routers

from author.views import LocationViewSet
from categories.views import CategoryViewSet
from home_work import settings
from home_work.settings import MEDIA_ROOT


router = routers.SimpleRouter()
router.register('location', LocationViewSet)
router.register('cat', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ad/', include('ads.urls')),
    # path('cat/', include('categories.urls')),
    path('user/', include('author.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)



