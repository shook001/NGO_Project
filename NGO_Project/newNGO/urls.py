from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', views.events, name='events'),
    path('event-detail/<int:id>/', views.event_detail, name='event_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

