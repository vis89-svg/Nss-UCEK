from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_name = form.cleaned_data.get('event_name')
            
            # If event_name is provided and already exists, use that name
            if event_name:
                existing_events = Event.objects.filter(event_name=event_name)
                if existing_events.exists():
                    # Use the provided event_name if it matches an existing event
                    form.instance.event_name = event_name
                else:
                    # If event_name does not exist, create a new event with the provided name
                    form.instance.event_name = event_name
            else:
                # If event_name is not provided, assume the last event's name
                last_event = Event.objects.last()
                if last_event:
                    form.instance.event_name = last_event.event_name
            
            form.save()
            return redirect('view_events')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def view_events(request):
    events = Event.objects.all().order_by('-date')

    # Initialize a dictionary to hold grouped events
    grouped_events = {}

    # Manually group events by event_name while preserving the order
    for event in events:
        if event.event_name not in grouped_events:
            grouped_events[event.event_name] = []  # Initialize a new list for each event_name
        grouped_events[event.event_name].append(event)

    return render(request, 'view_events.html', {
        'grouped_events': grouped_events,
    })
