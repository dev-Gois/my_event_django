from django_viewcomponent import component

@component.register('event_carousel')
class EventCarouselComponent(component.Component):
  template_name = 'event_carousel/event_carousel.html'

  def __init__(self, **kwargs):
    self.events = kwargs.get("events", [])