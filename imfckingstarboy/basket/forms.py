from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone_number', 'address', 'city', 'post_code', 'items']
        labels = {'full_name':'Ime i prezime',
                'phone_number': 'Broj telefona',
                'address': 'Adresa',
                'city': 'Grad', 
                'post_code':'Poštanski broj',
                'items': 'Porucene stvari'}
        
