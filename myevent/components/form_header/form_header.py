from django_viewcomponent import component

@component.register('form_header')
class FormHeaderComponent(component.Component):
  template_name = 'form_header/form_header.html'

  def __init__(self, **kwargs):
    self.title = kwargs.get("title", "")
    self.subtitle = kwargs.get("subtitle", "")