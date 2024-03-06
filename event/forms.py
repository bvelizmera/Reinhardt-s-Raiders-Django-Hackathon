from django import forms
from .models import Event, Student


class EventForm(forms.ModelForm):
    """
    Form class for users to create an event 
    """
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location',
            'course', 'interest', 'max_capacity', 'excerpt',)
