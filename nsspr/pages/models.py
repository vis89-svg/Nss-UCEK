
from django.db import models
from django.utils import timezone

class Pages(models.Model):
    event_name = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    day=models.CharField(max_length=100,null=True)
    description = models.TextField(blank=True, null=True)
    gphotos=models.CharField(max_length=700,null=True)
    image = models.ImageField(upload_to='event_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.event_name or 'Unnamed Event'} at {self.place}"
