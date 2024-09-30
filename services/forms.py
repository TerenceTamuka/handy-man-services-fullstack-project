from django import forms
from .models import Booking
from django_summernote.widgets import SummernoteWidget

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 'service', 'date_time','approved', 'additional_info']
        widgets = {
            'date_time': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'additional_info': SummernoteWidget(),  # Use Summernote widget for additional_info field
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Expecting 'user' to be passed when the form is initialized
        super(BookingForm, self).__init__(*args, **kwargs)
        
        # If the user is an admin (staff), include the 'approved' field
        if user and user.is_staff:
            self.fields['approved'] = forms.BooleanField(required=False)