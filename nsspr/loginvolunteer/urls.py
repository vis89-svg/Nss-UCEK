# events/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('search_volunteer/', views.login_view, name='volunteer_login'),
]
