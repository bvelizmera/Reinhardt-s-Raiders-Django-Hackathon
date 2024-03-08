"""

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.eventsDisplay, name='home'),
    path('new_student/', views.create_student, name='create_student'),
    path('non_student/', views.non_student, name='non_student'),
    path('event/', views.show_user_events, name='user_events'),
    path('event/<int:pk>', views.EventAttending, name='event_attending'),
    path('signup/', views.redirect_to_signup, name='redirect_to_signup'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('upload/', views.upload, name='upload_image'),
    path('profile/', views.profile, name='user_profile'),
    path('event/<int:pk>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
    path('event/<int:pk>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
]