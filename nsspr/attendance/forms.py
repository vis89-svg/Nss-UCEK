from django import forms
from .models import AttendanceEvent, AttendanceVolunteer, AttendanceRecord

class AttendanceEventForm(forms.ModelForm):
    class Meta:
        model = AttendanceEvent
        fields = ['name', 'date']

class AttendanceVolunteerForm(forms.ModelForm):
    class Meta:
        model = AttendanceVolunteer
        fields = ['name']

class MarkAttendanceForm(forms.Form):
    event = forms.ModelChoiceField(queryset=AttendanceEvent.objects.all(), label='Event')
    volunteers = forms.ModelMultipleChoiceField(
        queryset=AttendanceVolunteer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Select Volunteers'
    )
