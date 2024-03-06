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
    event = queryset.first()
    # toRender = HttpResponse(queryset)

    return render(request, 
        'event/event.html', 
        {"event": event,
        }
    )

def display_base(request):
    return render(request, 'base.html')