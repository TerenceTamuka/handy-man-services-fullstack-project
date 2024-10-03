from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/new/', views.create_booking, name='create_booking'),
    path('bookings/<int:pk>/edit/', views.update_booking,
         name='update_booking'),
    path('bookings/<int:pk>/delete/', views.delete_booking,
         name='delete_booking'),
    path('booking/edit/<int:booking_id>/', views.edit_booking,
         name='edit_booking'),
    path('register/', views.register, name='register'),
]
