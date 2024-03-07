"""

"""

from django.urls import path
from . import views
from .views import event_detail

urlpatterns = [
    path('', views.eventsDisplay, name='home'),
    path('new_student/', views.create_student, name='create_student'),
    path('non_student/', views.non_student, name='non_student'),
    path('event/', views.show_user_events, name='user_events'),
    path('event/<int:pk>', views.EventAttending, name='event_attending'),
    path('signup/', views.redirect_to_signup, name='redirect_to_signup'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]