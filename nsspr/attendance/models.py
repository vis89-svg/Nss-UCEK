from django.db import models

class AttendanceEvent(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name

class AttendanceVolunteer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AttendanceRecord(models.Model):
    volunteer = models.ForeignKey(AttendanceVolunteer, on_delete=models.CASCADE)
    event = models.ForeignKey(AttendanceEvent, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    date = models.DateField()  # Ensure this field is included

    class Meta:
        unique_together = ('volunteer', 'event', 'date')  # Prevent duplicate records

    def __str__(self):
        return f'{self.volunteer} - {self.event} - {self.date}'