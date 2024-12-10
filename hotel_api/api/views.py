from .models import Reservation, Room
from .serializers import ReservationSerializer, RoomSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import NotAdminUser
from rest_framework import viewsets


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, NotAdminUser]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]