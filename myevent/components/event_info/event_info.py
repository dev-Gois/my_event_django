from django_viewcomponent import component

@component.register('event_info')
class EventInfoComponent(component.Component):
  template_name = 'event_info/event_info.html'

  def __init__(self, **kwargs):
    self.event = kwargs.get("event", None)