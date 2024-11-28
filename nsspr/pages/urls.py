from django.urls import path
from . import views

urlpatterns = [
    path('call/', views.create_Pages, name='create_Pages'),
    path('seen/', views.view_Pages, name='view_Pages'),
]
