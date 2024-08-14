from django_viewcomponent import component

@component.register('login_button')
class LoginButtonComponent(component.Component):
  template_name = 'login_button/login_button.html'

  def __init__(self, **kwargs):
    self.text = kwargs.get('text', 'Login')