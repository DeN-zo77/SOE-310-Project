from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('booking/<int:pk>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('schedule/', views.appointment_list, name='appointment_list'),
    path('schedule/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
]
