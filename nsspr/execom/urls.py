from django.urls import path
from . import views
urlpatterns = [
    path('execom/',views.event,name='execom'),
]