from rest_framework import serializers
from api.models import Reservation, Room


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        
    def validate_end_date(self, value):
        """
        Check that end date is after start date
        """
        start_date = self.initial_data.get("start_date")
        
        if start_date:
            start_date = serializers.DateField().to_internal_value(start_date)
            if value <= start_date:
                raise serializers.ValidationError("Reservation end date must be later than start date.")
        
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'