from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Student, Event
from .forms import EventForm

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
    queryset = Event.objects.all().filter(creator=request.user)
    print(queryset)
    # Handle form data
    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.creator = request.user
            event.save()
            # messages.add_message(
            #     request, messages.SUCCESS,
            #     'Event submitted and awaiting approval'
            # )
    #Initialise empty form
    event_form = EventForm()

    return render(request, 
        'event/user_events.html', 
        {"events_queryset": queryset,
         "event_form": event_form,
        }
    )

def display_base(request):
    return render(request, 'base.html')