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
<<<<<<< HEAD
    path('register/', views.post),
    path('user-view/', TemplateView.as_view(template_name='user_view.html'), name='event'),
    path('event-details/', TemplateView.as_view(template_name='event_details.html'), name='event-details'),
    path('price/', TemplateView.as_view(template_name='total_price.html'), name='price'),
    path('conformation/', TemplateView.as_view(template_name='confirm.html'), name='conformation'),
]
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> 2e34e389c8963ae61f73a45da229d1cb010c2068
