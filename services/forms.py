from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 'service', 'date_time', 'additional_info']
        widgets = {
            'date_time': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        }