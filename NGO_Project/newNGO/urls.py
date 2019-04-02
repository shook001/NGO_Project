from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView

from app import views

urlpatterns = [
    path('', views.events, name='events'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('confirmation/', views.confirm, name='confirmation'),
    path('event-detail/<int:id>/', views.event_detail, name='event_detail'),

    #Must define these within views.py
    # path('register/', views.register, name='register'),
    # path('price/', views.total, name='total'),#must work on algo for this!!!!
]
