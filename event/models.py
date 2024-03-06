from django.db import models

# Create your models here.
class Event(models.Model):
    """
    Stores a single event related to :model:Student
    """
    name = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(Student, 
        on_delete=CASCADE, related_name="event_created")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    max_capacity = models.IntegerField()
    interest = models.CharField(max_length=200)
    attending = models.ForeignKey(Student, 
        on_delete=CASCADE, related_name="attending")

    def __str__(self):
        return f"{self.name} on {self.date} at {self.location} | created by {self.creator}"