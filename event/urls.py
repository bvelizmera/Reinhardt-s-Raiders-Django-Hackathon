"""

"""

from django.urls import path
from . import views
from .views import display_base

urlpatterns = [
    path('', views.eventsDisplay, name='home'),
    path('event/', views.show_user_events, name='user_events'),
    path('event/<int:pk>', views.EventAttending, name='event_attending'),
    path('../base/', display_base, name='display_base'),
]