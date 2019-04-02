from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Event, User

admin.site.unregister(Group)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'category', 'start_date', \
	                'end_date', 'e_start_time', 'e_end_time', 'location',\
	                'registrants', 'e_image', 'e_adult_price', 'e_child_price']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'email', 'role']