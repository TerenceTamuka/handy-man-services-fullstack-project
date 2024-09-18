from django.contrib import admin
from .models import Service, Booking
from django_summernote.admin import SummernoteModelAdmin

class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  # Use Summernote for the 'description' field


# Register your models here.
admin.site.register(Service)
admin.site.register(Booking)
