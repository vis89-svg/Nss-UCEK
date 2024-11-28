
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Event
from .forms import LoginForm
from django.contrib import messages
from decimal import Decimal
import json
from django.db import transaction
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST
from datetime import datetime



# Create your views here.
def login_view(request):
    # Handle login functionality
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            events = Event.objects.filter(user_name=user_name, password=password)

            if user_name == 'NSSUCEK@ADMIN' and password == '###ADMIN@2000###':
                return render(request, 'mark_attendance.html', {
                    'events': Event.objects.all(), 
                    'show_add_button': True,
                    'show_edit_button': True,
                    'show_delete_menu': True  # New flag for showing delete menu
                })
            elif events.exists():
                return render(request, 'mark_attendance.html', {
                    'events': events, 
                    'show_add_button': False,
                    'show_edit_button': False,
                    'show_delete_menu': False  # Don't show delete menu for other users
                })
            else:
                # If credentials are invalid, add an error message
                messages.error(request, 'Invalid username or password')
                return render(request,'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
