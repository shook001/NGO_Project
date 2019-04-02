from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import RegisterForm
from .models import *
from django.contrib.auth.decorators import login_required


# Events will act as homepage
def events(request): # good
	events = Event.objects.all()
	return render(request, 'events.html', {'events': events})

# Selected object will be directed heres
@login_required
def event_detail(request, id):# good
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
			obj.save()
			return HttpResponseRedirect('/price/')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})


# Accounts/login
def login(request):
	return render(request, 'registration.login.html')


# After user selects ticket amounts we need to provide a sum/total
def total(request):
	pass


# confirmation that order was recognized
def confirm(request):# good
	return render(request, 'confirm.html')


def price(request):
	return render(request, 'total_price.html')
