from django_viewcomponent import component

@component.register('logout_button')
class LogoutButtonComponent(component.Component):
  template_name = 'logout_button/logout_button.html'

  def __init__(self, **kwargs):
    self.text = kwargs.get("text", "Logout")