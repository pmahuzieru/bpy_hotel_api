from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    """
    Representa una habitacion de hotel

    Atributos
    - name (str): el nombre de la habitacion
    - description (str): la descripcion de la habitacion
    - price_per_night (Decimal): el precio
    - is_available (bool): si esta o no disponible
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField()

    def __str__(self):
        return f"Room [{self.name}]"


class Reservation(models.Model):
    """
    Representa una reservacion realizada por un usuario.

    Atributos:
        user (User): el usuario que hace la reservacion.
        room (Room): la habitacion que fue reservada.
        start_date (Date): fecha de inicio.
        end_date (Date): fecha de fin.
    """

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
