from django import forms
from .models import Appointment, ContactMessage


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client_name', 'client_phone', 'client_email', 'service', 'barber', 'date', 'time', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
