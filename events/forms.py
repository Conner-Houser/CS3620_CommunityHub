from django import forms 
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "location", "date_time"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full'
            }),
            'location': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full'
            }),
            'date_time': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'border border-gray-300 rounded-lg p-2 w-full'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full h-24'
            }),
        }

