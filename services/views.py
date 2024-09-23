from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service, Booking
from .forms import BookingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def index(request):
    services = Service.objects.all()
    context = {
        'services': services,
        'is_authenticated': request.user.is_authenticated  # Pass authentication status
    }
    return render(request, 'services/index.html', context)
    
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'services/my_bookings.html', {'bookings': bookings})

@login_required
def create_booking(request):
    # Get the service from the query parameter if it exists
    service_id = request.GET.get('service_id')
    service = None
    if service_id:
        service = get_object_or_404(Service, id=service_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Check for overlapping bookings
            overlapping_booking = Booking.objects.filter(
                service=booking.service,
                date_time=booking.date_time
            ).exists()

            if overlapping_booking:
                form.add_error(None, 'This service is already booked at the selected time.')
            else:
                booking.user = request.user
                booking.save()
                messages.success(request, 'Booking created successfully!')
                return redirect('my_bookings')
    else:
        form = BookingForm(initial={'service': service})
    
    return render(request, 'services/booking_form.html', {'form': form, 'service': service})

@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'services/booking_form.html', {'form': form})

@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return render(request, 'services/booking_confirm_delete.html', {'booking': booking})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

