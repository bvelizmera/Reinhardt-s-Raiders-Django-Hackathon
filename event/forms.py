from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Event, Student, Photo


class EventForm(forms.ModelForm):
    """
    Form class for users to create an event 
    """
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location',
            'course', 'interest', 'max_capacity', 'excerpt', 'photo')

class StudentForm(forms.ModelForm):
    """
    Form class for users to create their student profile
    """
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'bio', 'photo')

class PhotoForm(forms.ModelForm):
  class Meta:
      model = Photo
      fields = ('image',)