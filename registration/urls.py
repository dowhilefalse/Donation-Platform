from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.view_index, name='page_index'),
    path('contact', views.view_contact, name='page_contact'),
    path('contact2', views.view_contact2, name='page_contact2'),
    path('register', views.view_register, name='page_register'),
    path('about', views.view_about, name='page_about'),
    path('group1', views.view_group1, name='page_group1'),
    path('group11', views.view_group11, name='page_group11'),
    path('group12', views.view_group12, name='page_group12'),
    path('group2', views.view_group2, name='page_group2'),
    path('group3', views.view_group3, name='page_group3'),
    path('registerform', views.view_registerform, name='ajax_registerform'),
    path('phone-captcha', views.view_phone_captcha, name='ajax_phone_captcha'),
    path('login', views.view_login, name='page_login'),
    path('logout', views.view_logout, name='page_logout'),
]