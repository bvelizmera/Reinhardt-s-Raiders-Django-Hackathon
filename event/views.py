from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
# def EventList(request):
#     return HttpResponse("Hello, world!")

def display_base(request):
    return render(request, 'base.html')