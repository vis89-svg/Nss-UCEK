
from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=100)  # Username associated with the event
    password = models.CharField(max_length=100)  # Password for user authentication (if used for custom auth)
    event_amount = models.CharField(max_length=10, default='0')
    
    def __str__(self):
        return self.event_name  # Or whatever field you use to represent the event