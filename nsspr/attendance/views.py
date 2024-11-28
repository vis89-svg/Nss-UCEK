from django.shortcuts import render, redirect, get_object_or_404
from .models import AttendanceEvent, AttendanceVolunteer, AttendanceRecord
from .forms import AttendanceEventForm, AttendanceVolunteerForm

def add_event(request):
    if request.method == 'POST':
        form = AttendanceEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_event')  # Redirect to a page that lists all events
    else:
        form = AttendanceEventForm()
    return render(request, 'add_event.html', {'form': form})

def add_volunteer(request):
    if request.method == 'POST':
        form = AttendanceVolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_volunteer')  # Redirect to the volunteer list page
    else:
        form = AttendanceVolunteerForm()
    return render(request, 'add_volunteer.html', {'form': form})

def mark_attendance(request):
    events = AttendanceEvent.objects.all()
    volunteers = AttendanceVolunteer.objects.all()  # Adjust as needed

    if request.method == 'POST':
        event_id = request.POST.get('event')
        selected_event = get_object_or_404(AttendanceEvent, id=event_id)
        marked_volunteers = request.POST.getlist('marked_volunteers')
        date = selected_event.date  # Use the event date

        for volunteer_id in marked_volunteers:
            volunteer = get_object_or_404(AttendanceVolunteer, id=volunteer_id)
            # Create or update attendance record
            AttendanceRecord.objects.update_or_create(
                volunteer=volunteer,
                event=selected_event,
                defaults={'present': True, 'date': date}  # Set the date here
            )
        
        return redirect('attendance_display')

    return render(request, 'mark_attendance.html', {'events': events, 'volunteers': volunteers})

from django.shortcuts import render
from .models import AttendanceEvent, AttendanceRecord  # Ensure AttendanceRecord is the correct model

def attendance_display(request):
    search_query = request.GET.get('search', '')

    # Filter events based on the search query
    if search_query:
        events = AttendanceEvent.objects.filter(name__icontains=search_query)
    else:
        events = AttendanceEvent.objects.all()
    
    # Prepare a dictionary to store records grouped by event
    event_records = {}
    
    # Iterate through each event and get the records associated with it
    for event in events:
        records = AttendanceRecord.objects.filter(event=event)  # Adjust this if using a different model name
        event_records[event] = records
    
    return render(request, 'attendance_display.html', {'event_records': event_records})


def volunteer_list(request):
    volunteers = AttendanceVolunteer.objects.all()
    return render(request, 'volunteer_list.html', {'volunteers': volunteers})



from django.shortcuts import render
from .models import AttendanceEvent, AttendanceVolunteer, AttendanceRecord

def search_volunteer(request):
    volunteer_name = request.GET.get('volunteer_name', '')
    events_attended = []
    total_events = AttendanceEvent.objects.count()  # Total events count
    attended_count = 0
    attendance_percentage = 0

    if volunteer_name:
        volunteer = AttendanceVolunteer.objects.filter(name__iexact=volunteer_name).first()
        if volunteer:
            events_attended = AttendanceRecord.objects.filter(volunteer=volunteer, present=True)
            attended_count = events_attended.count()
            attendance_percentage = (attended_count / total_events) * 100 if total_events > 0 else 0

    context = {
        'volunteer_name': volunteer_name,
        'events_attended': events_attended,
        'total_events': total_events,
        'attended_count': attended_count,
        'attendance_percentage': attendance_percentage,
    }
    return render(request, 'search_volunteer.html', context)
