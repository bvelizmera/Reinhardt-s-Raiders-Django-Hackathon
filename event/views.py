from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Student, Event, Review
from .forms import EventForm, StudentForm, ReviewForm


# additional function
def is_viewer_student(request):
    print(f"Checking whether user {request.user} has a student profile")
    is_student=True
    try:
        student = get_object_or_404(Student, user=request.user)
    except:
        is_student=False
    else:
        print(student)
    return is_student

# Create your views here.
def eventsDisplay(request):
    """
    Display all events
    """
    queryset = Event.objects.all()
    is_student = is_viewer_student(request)

    return render(request, 
        'event/event.html', 
        {"event_queryset": queryset,
         "is_student": is_student,
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

def non_student(request):
    """
    Pass a non-student user to the student profile creation form
    """
    return HttpResponseRedirect(reverse('create_student'))

def redirect_to_signup(request):
    """
    Pass a non-registered user to the signup page
    """
    return HttpResponseRedirect(reverse('account_signup'))

def show_user_events(request):
    """
    Display all events created by the logged-in user
    """
    queryset = Event.objects.all().filter(creator=request.user)
    is_student = is_viewer_student(request)
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
    for event in queryset:
        print(event.photo)
        print(event.photo.url)

    return render(request, 
        'event/user_events.html', 
        {"events_queryset": queryset,
         "event_form": event_form,
         "is_student": is_student,
        }
    )

def create_student(request):
    """
    Display the form to allow a user to create their student profile
    """

    if request.method == "POST":
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.user = request.user
            student.username = request.user.username
            student.save()
            return HttpResponseRedirect(reverse('user_events'))
    
    student_form = StudentForm()

    return render(request,
        'event/new_student.html',
        {'student_form': student_form,
        }
    )


def event_detail(request, pk):

    queryset = Event.objects.all()

    event = get_object_or_404(queryset, pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.event = event
            review.author = request.user
            review.save()
           

    review_form = ReviewForm()
    return render(request,
        'event/event_detail.html',
        {'event': event,
         'review_form':review_form,
        }
    )


 