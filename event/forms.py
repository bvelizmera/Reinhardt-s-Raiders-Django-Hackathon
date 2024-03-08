from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Event, Student, Photo, Review


class EventForm(forms.ModelForm):
    """
    Form class for users to create an event 
    """

    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={'type': 'text'})
    )
    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    time = forms.TimeField(
        label='Time',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(attrs={'type': 'text'})
    )
    course = forms.CharField(
        label='Course',
        widget=forms.TextInput(attrs={'type': 'text'})
    )
    interest = forms.CharField(
        label='Interest',
        widget=forms.TextInput(attrs={'type': 'text'})
    )
    max_capacity = forms.IntegerField(
        label='Max Capacity',
        widget=forms.NumberInput(attrs={'type': 'number'})
    )
    excerpt = forms.CharField(
        label='Excerpt',
        widget=forms.Textarea(attrs={'type': 'text','rows': 4, 'cols': 40})
    )
    photo_url = forms.CharField(
        label='Photo URL',
        widget=forms.TextInput(attrs={'type': 'text'})
    )
    # photo = forms.CloudinaryFileField(
    #     label='Photo',
    #     widget=forms.FileInput(attrs={'type': 'file'})
    # )
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location',
            'course', 'interest', 'max_capacity', 'excerpt', 'photo_url')

class StudentForm(forms.ModelForm):
    """
    Form class for users to create their student profile
    """
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'bio', 'photo_url')

class PhotoForm(forms.ModelForm):
  class Meta:
      model = Photo
      fields = ('image',)

class ReviewForm(forms.ModelForm):
    """
    Form class for users to create their review
    """
    class Meta:
        model = Review
        fields = ('body', 'rating', 'has_attended')