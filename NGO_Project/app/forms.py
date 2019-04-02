from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(label='Phone Number', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    adultQty = forms.CharField(label='Adult Quantity', max_length=2)
    childQty = forms.CharField(label='Child Quantity', max_length=2)

