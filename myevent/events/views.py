from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Schedule
from django.utils import timezone
from django.contrib import messages
from .forms import ScheduleForm, EventForm

def format_event(event):
    return {
        'id': event.id,
        'name': event.name,
        'type': event.get_type_display(),
        'initial_date': event.start_date.strftime("%d/%m/%Y"),
        'final_date': event.end_date.strftime("%d/%m/%Y"),
        'local': event.local,
        'city': event.city,
        'state': event.state,
        'ticket_price': event.ticket_price,
        'limited_tickets': event.limited_tickets,
        'ticket_quantity': event.ticket_quantity,
    }

def format_schedule(schedule):
    return {
        'id': schedule.id,
        'date': schedule.date.strftime("%d/%m/%Y"),
        'time': schedule.time.strftime("%H:%M"),
    }

def dashboard(request):
    today = timezone.now().date()
    events = []
    
    for event in Event.objects.filter(start_date__gte=today):
        schedules = Schedule.objects.filter(event=event).first()
        events.append({
            **format_event(event),
            'start_time': schedules.time.strftime("%H:%M") if schedules else '',
        })

    return render(request, 'dashboard.html', {
        'user_name': request.user.username.capitalize(),
        'today_events': len(events),
        'events': events
    })

def events(request):
    events = []
    
    for event in Event.objects.all():
        schedules = Schedule.objects.filter(event=event).first()
        events.append({
            **format_event(event),
            'organizer': event.user.username,
            'user_is_organizer': event.user == request.user,
            'start_time': schedules.time.strftime("%H:%M") if schedules else '',
        })

    return render(request, 'events.html', {
        'events': events
    })

def event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    schedules = [format_schedule(schedule) for schedule in Schedule.objects.filter(event=event)]
    user_is_organizer = event.user == request.user

    return render(request, 'event.html', {
        'event': format_event(event),
        'schedules': schedules,
        'user_is_organizer': user_is_organizer,
    })

def user_events(request):
    events = []

    for event in Event.objects.filter(user=request.user):
        events.append({
            **format_event(event),
            'user_is_organizer': True
        })

    return render(request, 'user_events.html', {
        'events': events
    })

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()

    messages.success(request, 'Evento deletado com sucesso!')
    return redirect('user_events')

def create_event(request):
    form_class = EventForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            messages.success(request, 'Evento criado com sucesso!')
            return redirect('user_events')
        else:
            messages.error(request, 'Erro ao criar evento!')
            return render(request, 'new_event.html', {
                'form': form
            })
    else:
        form = form_class()

    return render(request, 'new_event.html', {
        'form': form
    })

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    form_class = EventForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=event)
        form.start_date = event.start_date.strftime("%d/%m/%Y")
        form.end_date = event.end_date.strftime("%d/%m/%Y")
        if form.is_valid():
            form.save()

            messages.success(request, 'Evento editado com sucesso!')
            return redirect('user_events')
        else:
            messages.error(request, 'Erro ao editar evento!')
            return render(request, 'edit_event.html', {
                'form': form,
            })
    else:
        form = form_class(instance=event,initial={
            'start_date': event.start_date.strftime("%d/%m/%Y"),
            'end_date': event.end_date.strftime("%d/%m/%Y")
        })

    return render(request, 'edit_event.html', {
        'form': form
    })

def create_schedule(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form_class = ScheduleForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.event = event
            schedule.save()

            messages.success(request, 'Agenda criada com sucesso!')
            return redirect('event', event_id)
        else:
            messages.error(request, 'Erro ao criar agenda!')
            return render(request, 'new_schedule.html', {
                'form': form,
                'event': format_event(event)
            })
    else:
        form = form_class(
            start_date=event.start_date.strftime("%Y-%m-%d"),
            end_date=event.end_date.strftime("%Y-%m-%d")
        )

    return render(request, 'new_schedule.html', {
        'form': form,
        'event': format_event(event)
    })

def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    event_id = schedule.event.id
    schedule.delete()

    messages.success(request, 'Agenda deletada com sucesso!')
    return redirect('event', event_id)

def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    event = schedule.event
    form_class = ScheduleForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=schedule)
        if form.is_valid():
            form.save()

            messages.success(request, 'Agenda editada com sucesso!')
            return redirect('event', event.id)
        else:
            messages.error(request, 'Erro ao editar agenda!')
            return render(request, 'edit_schedule.html', {
                'form': form,
            })
    else:
        form = form_class(instance=schedule)

    return render(request, 'edit_schedule.html', {
        'form': form,
        'schedule_id': schedule_id,
        'schedule': format_schedule(schedule),
        'event': format_event(event)
    })