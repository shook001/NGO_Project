from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', views.events, name='events'),
    path('event-detail/<int:id>/', views.event_detail, name='event_detail'),

]
