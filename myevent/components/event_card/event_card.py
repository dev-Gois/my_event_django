from django_viewcomponent import component

@component.register('event_card')
class EventCardComponent(component.Component):
  template_name = 'event_card/event_card.html'

  def __init__(self, **kwargs):
    self.event = kwargs.get("event", None)