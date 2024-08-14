from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('events/', include('events.urls')),
    path('', index, name='index'),
]
