from django.db import models
from django.contrib.auth.models import User
from event.models import Event


STATUS = ((1, "1",), (2, "2",), (3, "3",), (4, "4",), (5, "5",))

# Create your models here.

class Review (models.Model):
    event = models.ForeignKey(Event,
        on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User,
        on_delete=models.CASCADE, related_name="reviewer")
    body = models.TextField(max_length=1000)
    has_attended = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(choices=STATUS, blank=True)
    
    def __str__(self):
        return f"Review {self.body} by {self.author} on {self.updated_on}"

