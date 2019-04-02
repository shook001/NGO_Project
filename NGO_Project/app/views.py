from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import RegisterForm
from .models import *


def events(request):
	events = Event.objects.all()
	return render(request, 'events.html', {'events': events})


def event_detail(request, id):
	try:
		event = Event.objects.get(id=id)
	except Event.DoesNotExist:
		raise Http404('Event not found!!')
	return render(request, 'event-detail.html', {'event': event})


def post(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			obj = RegForm()
			obj.first_name = form.cleaned_data['first_name']
			obj.last_name = form.cleaned_data['last_name']
			obj.email = form.cleaned_data['email']
			obj.phone = form.cleaned_data['phone']
			obj.address = form.cleaned_data['address']
			obj.adultQty = form.cleaned_data['adultQty']
			obj.childQty = form.cleaned_data['childQty']
			return HttpResponseRedirect('/price/')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

	# form = RegisterForm()
	# return render(request, 'register.html', {'form': form})

