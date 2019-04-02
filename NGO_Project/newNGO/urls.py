from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('', views.events, name='events'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('confirmation/', views.confirm, name='confirmation'),
    path('event-detail/<int:id>/', views.event_detail, name='event_detail'),
    path('register/', views.post),
    path('event-details/', TemplateView.as_view(template_name='event_details.html'), name='event-details'),
    path('price/', TemplateView.as_view(template_name='total_price.html'), name='price'),
    path('conformation/', TemplateView.as_view(template_name='confirm.html'), name='conformation'),
]