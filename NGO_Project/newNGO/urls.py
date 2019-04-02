from django.contrib import admin
from django.urls import path, include
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
    path('price/', views.price, name='price')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)