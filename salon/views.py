from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, Barber, Appointment
from .forms import AppointmentForm, ContactForm


def home(request):
    """Landing page: shop intro plus a preview of featured services."""
    featured_services = Service.objects.all()[:3]
    return render(request, 'salon/home.html', {'featured_services': featured_services})


def about(request):
    """Static page describing the shop and its barbers."""
    barbers = Barber.objects.all()
    return render(request, 'salon/about.html', {'barbers': barbers})


def services(request):
    """Full list of services offered, with prices and durations."""
    all_services = Service.objects.all()
    return render(request, 'salon/services.html', {'services': all_services})


def contact(request):
    """Show a contact form on GET; save the message and confirm on valid POST."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your message has been sent — we'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'salon/contact.html', {'form': form})


def book_appointment(request):
    """Show the booking form on GET; validate and save a new Appointment on POST."""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('booking_confirmation', pk=appointment.pk)
    else:
        form = AppointmentForm()
    return render(request, 'salon/booking_form.html', {'form': form})


def booking_confirmation(request, pk):
    """Thank-you page showing the details of a just-made booking."""
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'salon/booking_confirmation.html', {'appointment': appointment})


def appointment_list(request):
    """Owner-facing view of every booked appointment, soonest first."""
    appointments = Appointment.objects.all()
    return render(request, 'salon/appointment_list.html', {'appointments': appointments})


def appointment_delete(request, pk):
    """Confirm on GET, delete the appointment on POST."""
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'salon/appointment_confirm_delete.html', {'appointment': appointment})
