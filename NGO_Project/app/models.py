from django.db import models



class Event(models.Model):
	EVENT_CHOICES = {
		('Con', 'Conference'),
		('Sem', 'Seminar'),
		('Pres', 'Presentation')
	}
	name = models.CharField(max_length=35)
	description = models.TextField(max_length=255)
	category = models.CharField(choices=EVENT_CHOICES, max_length=4)
	start_date = models.DateField()
	end_date = models.DateField()
	e_start_time = models.DateTimeField()
	e_end_time = models.DateTimeField()
	location = models.CharField(max_length=50)
	registrants = models.BooleanField()
	e_image = models.ImageField()
	e_adult_price = models.DecimalField(max_digits=5, decimal_places=2)
	e_child_price = models.DecimalField(max_digits=5, decimal_places=2)


class User(models.Model):
	ROLE_CHOICES = [('U', 'User'), ('A', 'Admin')]
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	email = models.CharField(max_length=25)
	password = models.CharField(max_length=20)
	"""Testing blank=True on role. If any problems arise, let Ed know."""
	role = models.CharField(choices=ROLE_CHOICES, max_length=5, blank=True)


class RegForm(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	adultQty = models.CharField(max_length=2)
	childQty = models.CharField(max_length=2)