from django_flatpickr.widgets import DatePickerInput, TimePickerInput
from django_flatpickr.schemas import FlatpickrOptions
from .models import Event, Schedule
from django import forms
from datetime import datetime

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Nome do Evento'
        self.fields['type'].label = 'Tipo de Evento'
        self.fields['start_date'].label = 'Data de Início'
        self.fields['end_date'].label = 'Data de Término'
        self.fields['local'].label = 'Local'
        self.fields['city'].label = 'Cidade'
        self.fields['state'].label = 'Estado'
        self.fields['ticket_price'].label = 'Preço do Ingresso'
        self.fields['limited_tickets'].label = 'Ingressos Limitados'
        self.fields['ticket_quantity'].label = 'Quantidade de Ingressos'
        
    class Meta:
        model = Event
        fields = ['name', 'type', 'start_date', 'end_date', 'local', 'city', 'state', 'ticket_price', 'limited_tickets', 'ticket_quantity']
class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        min_date = kwargs.pop('start_date', None)
        max_date = kwargs.pop('end_date', None)

        super().__init__(*args, **kwargs)

        self.fields['date'].widget = DatePickerInput(
            options=FlatpickrOptions(
                minDate=min_date or "today",
                maxDate=max_date or "today",
                defaultDate="today",
                locale="pt",
                altInputClass="form-input",
            )
        )
        
        self.fields['time'].widget = TimePickerInput(
            options=FlatpickrOptions(
                locale="pt",
                altInputClass="form-input",
                time_24hr=True,
                enableSeconds=False,
            )
        )
    class Meta:
        model = Schedule
        fields = ['date', 'time']