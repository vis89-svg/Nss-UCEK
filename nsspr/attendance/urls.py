from django.urls import path
from . import views

urlpatterns = [
    path('add_event/', views.add_event, name='add_event'),
    path('add_volunteer/', views.add_volunteer, name='add_volunteer'),  # Ensure this line exists
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance_display/', views.attendance_display, name='attendance_display'),
    path('volunteer_list/', views.volunteer_list, name='volunteer_list'),  # Add this line
    path('search_volunteer/', views.search_volunteer, name='search_volunteer'),
]
