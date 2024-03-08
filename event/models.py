from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student(models.Model):
    """
    Stores a single student related to :models.auth.user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    photo = CloudinaryField('image', default='placeholder', blank=True)

    def __str__(self):
        return f"{self.username}"
 
# @receiver(post_save, sender=User)
# def create_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance, username=instance.username)

# @receiver(post_save, sender=User)
# def save_student(sender, instance, **kwargs):
#     instance.profile.save()


class Event(models.Model):
    """
    Stores a single event related to :model:Student
    """
    name = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name="event_created")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    max_capacity = models.IntegerField()
    interest = models.CharField(max_length=200)
    attending = models.ManyToManyField(Student, 
        related_name="attending", blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    photo = CloudinaryField('image', default='placeholder', blank=True)

    def __str__(self):
        return f"{self.name} on {self.date} at {self.location} | created by {self.creator}"

    def number_attending(self):
        return self.attending.count()

class Photo(models.Model):
  image = CloudinaryField('image')