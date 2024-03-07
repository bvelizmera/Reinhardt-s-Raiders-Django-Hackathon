from django.shortcuts import render
from django.http import HttpResponse
from event.models import Event, Student
from .models import Review


# Create your views here.

def my_review(request):
    queryset = Review.objects.all()
    return HttpResponse(queryset.first())