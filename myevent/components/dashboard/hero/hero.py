from django_viewcomponent import component

@component.register('dashboard_hero')
class DashboardHeroComponent(component.Component):
  template_name = 'dashboard/hero/hero.html'

  def __init__(self, **kwargs):
    self.today_events = kwargs.get("today_events", 0)
    if kwargs.get("user_name") is not "":
      self.user_name = kwargs.get("user_name").capitalize()
    else:
      self.user_name = "Fulano"