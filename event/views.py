from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Student, Event

# Create your views here.
def EventList(request):
    """
    Display all events
    """
    queryset = Event.objects.all()
    # event = get_object_or_404(queryset, creator=request.user)

    return render(request, 
        'event/event.html', 
        {"event_queryset": queryset,
        }
    )

def show_user_events(request):
    """
    Display all events created by the logged-in user
    """
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, creator=request.user)

    return render(request, 
        'event/user_events.html', 
        {"event": event,
        }
    )

def display_base(request):
    return render(request, 'base.html')