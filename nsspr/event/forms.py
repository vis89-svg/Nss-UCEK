from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [ 'image', 'date',]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            
        }
