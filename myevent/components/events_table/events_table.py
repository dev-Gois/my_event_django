from django_viewcomponent import component

@component.register('events_table')
class EventsTableComponent(component.Component):
  template_name = 'events_table/events_table.html'

  def __init__(self, **kwargs):
    self.events = kwargs.get("events", [])
    self.user_is_organizer = kwargs.get("user_is_organizer", False)
    self.type = kwargs.get("type", "all")