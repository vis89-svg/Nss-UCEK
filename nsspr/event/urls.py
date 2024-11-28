from django.urls import path
from .views import upload_card, view_cards, upcoming_events

urlpatterns = [
    path('upload/', upload_card, name='upload_card'),
    path('view/', view_cards, name='view_cards'),
    path('upcoming/', upcoming_events, name='upcoming_events'),
]
