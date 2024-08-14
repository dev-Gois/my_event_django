from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_function, logout as logout_function
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
  if request.user.is_authenticated:
    messages.error(request, 'Você já está logado')
    return redirect('dashboard')
  if request.method == "GET":
    return render(request, 'authentication/login.html', {})
  elif request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(email=email).first()
    if user:
      user = authenticate(request, username=user.username, password=password)
      print(user)
      if user is not None:
        login_function(request, user)
        messages.success(request, 'Login realizado com sucesso')
        return redirect('dashboard')
      else:
        messages.error(request, 'Email ou senha inválidos')
        return redirect('login')
    else:
      messages.error(request, 'Email ou senha inválidos')
      return redirect('login')

def register(request):
  if request.user.is_authenticated:
    messages.error(request, 'Você já está logado')
    return redirect('dashboard')
  if request.method == "GET":
    return render(request, 'authentication/register.html', {})
  elif request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    user = User.objects.filter(email=email).first()
    user_name = User.objects.filter(username=name).first()

    if user:
      messages.error(request, 'Email já cadastrado')
      return redirect('register')
    if user_name:
      messages.error(request, 'Nome de usuário já cadastrado')
      return redirect('register')
    if password != confirm_password:
      messages.error(request, 'Senhas não coincidem')
      return redirect('register')
    
    new_user = User.objects.create_user(username=name, email=email, password=password)
    new_user.save()
    if new_user:
      login_function(request, new_user)
      messages.success(request, 'Cadastro realizado com sucesso')
      return redirect('dashboard')
    
def logout(request):
  if request.user.is_authenticated:
    messages.success(request, 'Logout realizado com sucesso')
    logout_function(request)
    return redirect('login')
  else:
    messages.error(request, 'Você não está logado')
    return redirect('login')