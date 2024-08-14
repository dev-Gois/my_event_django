from django_viewcomponent import component

@component.register('schedules_table')
class SchedulesTableComponent(component.Component):
  template_name = 'schedules_table/schedules_table.html'

  def __init__(self, **kwargs):
    self.schedules = kwargs.get("schedules", [])
    self.type = kwargs.get("type", "all")
