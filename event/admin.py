from django.contrib import admin
from .models import Student, Event
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('name', 'creator', 'location', 'date', 'time')
    search_fields = ['title', 'location']
    list_filter = ('creator', 'date')
    prepopulated_fields = {}
    summernote_fields = ('excerpt',)


# Register your models here.
admin.site.register(Student)