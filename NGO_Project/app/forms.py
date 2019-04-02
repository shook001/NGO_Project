from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(label='Phone Number', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    adultQty = forms.IntegerField(label='Adult Quantity')
    childQty = forms.IntegerField(label='Child Quantity')