from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('events/', views.events, name='events'),
    path('event-detail/<int:id>/', views.event_detail, name='event_detail'),
    path('user-view/', TemplateView.as_view(template_name='user_view.html'), name='event'),
    path('event-details/', TemplateView.as_view(template_name='event_details.html'), name='event-details'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('price/', TemplateView.as_view(template_name='total_price.html'), name='price'),
    path('conformation/', TemplateView.as_view(template_name='confirm.html'), name='conformation'),
]
