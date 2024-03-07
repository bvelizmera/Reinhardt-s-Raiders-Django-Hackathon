from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Student, Event
from .forms import EventForm

# Create your views here.
def eventsDisplay(request):
    """
    Display all events
    """
    queryset = Event.objects.all()
    student = get_object_or_404(Student, user=request.user)

    return render(request, 
        'event/event.html', 
        {"event_queryset": queryset,
         "student_id": student.id,
        }
    )

def EventAttending(request, pk):
    """
    Handle student clicking to attend an event by updating Event.attending.
    derived from https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg
    """
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    student = get_object_or_404(Student, user=request.user)
    if event.attending.filter(id=student.id).exists():
        event.attending.remove(student)
    else:
        event.attending.add(student)
    print(student.attending.filter(id=1))
    print(event.attending.count())

    return HttpResponseRedirect(reverse('home'))

def show_user_events(request):
    """
    Display all events created by the logged-in user
    """
    queryset = Event.objects.all().filter(creator=request.user)
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