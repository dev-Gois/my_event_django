from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('', views.events, name='events'),
  path('<int:event_id>/', views.event, name='event'),
  path('user_events/', views.user_events, name='user_events'),
  path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
  path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
  path('create_event/', views.create_event, name='create_event'),
  path('<int:event_id>/create_schedule/', views.create_schedule, name='create_schedule'),
  path('delete_schedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
  path('edit_schedule/<int:schedule_id>/', views.edit_schedule, name='edit_schedule'),
]