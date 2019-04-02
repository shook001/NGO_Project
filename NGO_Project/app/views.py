from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Event, User

# Events will act as homepage
def events(request): # good
	events = Event.objects.all()
	return render(request, 'events.html', {'events': events})

# Selected object will be directed here
def event_detail(request, id):# good
	try:
		event = Event.objects.get(id=id)
	except Event.DoesNotExist:
		raise Http404('Event not found!!')
	return render(request, 'event-detail.html', {'event': event})


# Accounts/login
def login(request):
	return render(request, 'registration.login.html')

# After user selects ticket amounts we need to provide a sum/total
def total(request):
	pass


# confirmation that order was recognized
def confirm(request):# good
	return render(request, 'confirm.html')
