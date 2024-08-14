from django.contrib import admin
from .models import Event, Schedule

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'local', 'city', 'state', 'ticket_price', 'limited_tickets', 'ticket_quantity')
    list_filter = ('type', 'city', 'state', 'limited_tickets')
    search_fields = ('name', 'local', 'city', 'state')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'time')
    list_filter = ('event', 'date')
    search_fields = ('event__name',)
    ordering = ('event', 'date', 'time')