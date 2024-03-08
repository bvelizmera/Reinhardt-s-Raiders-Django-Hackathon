from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import cl_init_js_callbacks
from .models import Student, Event, Review
from .forms import EventForm, StudentForm, PhotoForm, ReviewForm


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
    context = dict( backend_form = EventForm())
    # Handle form data
    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.creator = request.user
            # event.photo.url = event.photo_url
            print(event.photo_url)
            print(event)
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
    event_instance = Event.objects.get(pk__contains=pk)
    print(event_instance)

    event = get_object_or_404(queryset, pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.event = event
            review.author = request.user
            review.save()
           
    reviews = event_instance.reviews.all()

    review_form = ReviewForm()
    return render(request,
        'event/event_detail.html',
        {'event': event,
         'review_form':review_form,
         'reviews': reviews,
        }
    )

def review_edit(request, pk, review_id):
    """
    Display an individual review for edit.

    **Context**

    ``event``
        An instance of :model:`event.Event`.
    ``review``
        A single review related to the event.
    ``review_form``
        An instance of :form:`event.ReviewForm`
    """
    print("In review_edit")
    if request.method == "POST":
        event = get_object_or_404(Event, pk=pk)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.event = event
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                'Error updating review!')

    return HttpResponseRedirect(reverse('event_detail', args=[pk]))

def review_delete(request, pk, review_id):
    """
    view to delete review
    """
    
    review = get_object_or_404(Review, pk=review_id)
    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('event_detail', args=[pk]))

def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'event/upload.html', context)

def profile(request):

    student=request.user
    print(Student.user)
    
    profile = get_object_or_404(Student, user=request.user)
    events = Event.objects.filter(attending__username__contains=request.user)
    
    
    return render(request,
        'event/user_profile.html',
        {'profile': profile,
        'events': events,
        }
    )

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Successful login
            return redirect('success_page')  # Replace with your success page
        else:
            # Unsuccessful login
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')   


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Replace with your login URL
        else:
            # Unsuccessful registration
            messages.error(request, 'Invalid registration. Please correct the errors below.')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
