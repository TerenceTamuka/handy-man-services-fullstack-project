from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone


class Service(models.Model):
    SERVICE_CHOICES = [
        ('Painting', 'Painting - Price from £100'),
        ('Assembling', 'Assembling Furniture and Units - Price from £50'),
        ('Packing & Moving', 'Packing & Moving - Price from £100'),
    ]

    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    date_time = models.DateTimeField()
    additional_info = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)  # Approvings

    def __str__(self):
        return (
            f"{self.customer_name} - "
            f"{self.service.name} on {self.date_time}"
        )

    class Meta:
        unique_together = ['date_time', 'service']  # Prevent booking conflicts
