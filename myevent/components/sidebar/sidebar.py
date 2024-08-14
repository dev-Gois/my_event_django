from django_viewcomponent import component

@component.register('sidebar')
class SidebarComponent(component.Component):
  template_name = 'sidebar/sidebar.html'

  def __init__(self, **kwargs):
    self.title = kwargs.get("title", "")