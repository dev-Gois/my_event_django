from django_viewcomponent import component

@component.register('button')
class ButtonComponent(component.Component):
  template_name = 'button/button.html'

  def __init__(self, **kwargs):
    self.content = kwargs.get("content", "")
    self.type = kwargs.get("type", "button")
    self.variant = kwargs.get("variant", "primary")