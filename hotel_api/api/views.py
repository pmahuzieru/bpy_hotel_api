from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objetcs.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]