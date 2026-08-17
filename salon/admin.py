from django.contrib import admin
from .models import Service, Barber, Appointment, ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes')


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'barber', 'date', 'time')
    list_filter = ('date', 'barber', 'service')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
