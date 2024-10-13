# service_requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/<int:request_id>/', views.track_request, name='track_request'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
]
