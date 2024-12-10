from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price_per_night = models.DecimalField(decimal_places=2)
    is_available = models.BooleanField()

    def __str__(self):
        return f"Room [{self.name}]"


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reservations"
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="reservations"
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Reservation {self.room}, {self.start_date} - {self.end_date}"
