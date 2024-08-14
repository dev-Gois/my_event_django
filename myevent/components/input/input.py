from django_viewcomponent import component

@component.register('input')
class InputComponent(component.Component):
  template_name = 'input/input.html'

  def __init__(self, **kwargs):
    self.name = kwargs.get("name", "")
    self.placeholder = kwargs.get("placeholder", "")
    self.type = kwargs.get("type", "text")
    self.required = kwargs.get("required", False)