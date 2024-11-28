from django.db import models
from django.utils import timezone

class Card(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date
    date = models.DateField(default=timezone.now)  # Field for date input
    
    def __str__(self):
        # Return a meaningful representation, such as the date or other field you want to use
        return f"Card created on {self.date}"
