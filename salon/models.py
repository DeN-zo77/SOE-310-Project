from django.db import models


class Service(models.Model):
    """A haircut/grooming service the barbershop offers, with its price and duration."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=30)

    def __str__(self):
        return f"{self.name} (₦{self.price})"


class Barber(models.Model):
    """A barber who works at the shop."""
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """A client's booking for a service, optionally with a preferred barber."""
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)
    client_email = models.EmailField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="appointments")
    barber = models.ForeignKey(Barber, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.service.name} on {self.date} at {self.time}"

    class Meta:
        ordering = ['date', 'time']


class ContactMessage(models.Model):
    """A message submitted through the Contact page."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
