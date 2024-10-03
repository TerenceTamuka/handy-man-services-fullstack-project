from django.contrib import admin
from .models import Service, Booking
from django_summernote.admin import SummernoteModelAdmin


class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = (
        'description',
        'additional_info',  # Use Summernote for description and additional
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'customer_name',
        'service',
        'date_time',
        'approved'  # Show approved status in the list view
    ]
    list_filter = [
        'approved',
        'date_time'  # Add filters for approved status and date
    ]
    actions = ['approve_bookings']  # Add custom action

    def approve_bookings(self, request, queryset):
        """
        Custom admin action to approve bookings.
        """
        queryset.update(approved=True)
        self.message_user(request, "Selected bookings have been approved.")

    approve_bookings.short_description = "Approve selected bookings"


# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking, BookingAdmin)
