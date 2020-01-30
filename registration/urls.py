from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.view_index, name='page_index'),
    path('contact', views.view_contact, name='page_contact'),
    path('register', views.view_register, name='page_register'),
    path('about', views.view_about, name='page_about'),
    path('group1', views.view_group1, name='page_group1'),
    path('group11', views.view_group11, name='page_group11'),
    path('group12', views.view_group12, name='page_group12'),
    path('group2', views.view_group2, name='page_group2'),
    path('group3', views.view_group2, name='page_group3'),
]