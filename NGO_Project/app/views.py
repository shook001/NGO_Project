from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import RegisterForm
from .models import *
from django.contrib.auth.decorators import login_required


# Events will act as homepage
def events(request): # good
	events = Event.objects.all()
	return render(request, 'events.html', {'events': events})

# Selected object will be directed her
@login_required
def event_detail(request, id):# good
	try:
		event = Event.objects.get(id=id)
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
		else:
			form = RegisterForm()
		forms = RegForm.objects.latest('id')
		adult = forms.adultQty
		child = forms.childQty
		total = event.e_adult_price * forms.adultQty + event.e_child_price * forms.childQty
	except Event.DoesNotExist:
		raise Http404('Event not found!!')
	context = {
		'event': event,
		'form': form,
		'total': total,
		'adult': adult,
		'child': child
	}
	return render(request, 'event-detail.html', context)


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
