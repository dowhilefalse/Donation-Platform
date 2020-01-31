"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from api import views as api_views


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'organizations', api_views.OrganizationViewSet)
router.register(r'organization-contacts', api_views.OrganizationContactViewSet)
router.register(r'organization-demands', api_views.OrganizationDemandViewSet)

router.register(r'teams', api_views.TeamViewSet)
router.register(r'team-contacts', api_views.TeamContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('', include('registration.urls')),
]
