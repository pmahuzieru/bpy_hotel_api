from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import NotAdminUser
from rest_framework import viewsets


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API para gestionar las reservas.

    Metodos soportados:
    - GET: Lista todas las reservas.
    - POST: Crea una nueva reserva.
    - PUT: Actualiza una reserva existente.
    - DELETE: Elimina una reserva.

    Permisos:
    - Solo los usuarios autenticados que no sean administradores pueden acceder.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, NotAdminUser]


class RoomViewSet(viewsets.ModelViewSet):
    """
    API para gestionar las habitaciones.

    Metodos soportados:
    - GET: Lista todas las habitaciones.
    - POST: Crea una nueva habitacion.
    - PUT: Actualiza una habitacion existente.
    - DELETE: Elimina una habitacion.

    Permisos:
    - Solo los administradores autenticados pueden acceder.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]