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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.templatetags.staticfiles import static as static_url
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import include, path, re_path, resolve, Resolver404
from rest_framework import routers

from api import views as api_views


admin.site.site_header = '捐赠平台•管理'
admin.site.index_title = '后台主页'
admin.site.site_title = '管理后台'

favicon_view = RedirectView.as_view(url=static_url('favicon.png'), permanent=True)
robots_view = RedirectView.as_view(url=static_url('robots.txt'), permanent=True)

router = routers.DefaultRouter()
router.register(r'images', api_views.ImageViewSet)
router.register(r'users', api_views.UserViewSet)
router.register(r'organizations', api_views.OrganizationViewSet)
router.register(r'organization-contacts', api_views.OrganizationContactViewSet)
router.register(r'organization-demands', api_views.OrganizationDemandViewSet)

router.register(r'teams', api_views.TeamViewSet)
router.register(r'team-contacts', api_views.TeamContactViewSet)

urlpatterns = [
    re_path(r'^favicon\.png$', favicon_view, name='favicon_png'),
    re_path(r'^robots\.txt$', robots_view, name='robots_txt'),
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('filer/', include('filer.urls')),
    path('', include('registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
try:
    resolve('/static/favicon.png')
except Resolver404:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)