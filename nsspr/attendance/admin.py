from django.contrib import admin
from . models import AttendanceEvent
from . models import AttendanceVolunteer
from . models import AttendanceRecord
# Register your models here.
admin.site.register(AttendanceEvent)
admin.site.register(AttendanceVolunteer)
admin.site.register(AttendanceRecord)
