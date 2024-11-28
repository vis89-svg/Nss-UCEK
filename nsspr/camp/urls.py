from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_event, name='create_event'),
    path('show/', views.view_events, name='view_events'),
]
