from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    class EventType(models.TextChoices):
        SHOW_MUSICAL = '1', 'Show Musical'
        PECA_TEATRO = '2', 'Peça de Teatro'
        PALESTRA = '3', 'Palestra'
        ORQUESTRA = '4', 'Orquestra'
        STAND_UP_COMEDY = '5', 'Stand-up Comedy'
        SHOW_MAGICA = '6', 'Show de Mágica'
        SHOW_DANCA = '7', 'Show de Dança'
        OUTRO = '8', 'Outro'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=2, choices=EventType.choices, default=EventType.OUTRO)
    name = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)
    limited_tickets = models.BooleanField()
    ticket_quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def is_free(self):
        return self.ticket_price == 0

class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.date} {self.time}'