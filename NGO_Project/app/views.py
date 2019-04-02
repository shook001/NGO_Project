from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Event


def events(request):
	events = Event.objects.all()
	return render(request, 'events.html', {'events': events})


def event_detail(request, id):
	try:
		event = Event.objects.get(id=id)
	except Event.DoesNotExist:
		raise Http404('Event not found!!')
	return render(request, 'event-detail.html', {'event': event})
