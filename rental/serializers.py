from rest_framework import serializers

from core.models import Rental, Reservation


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = '__all__'
        read_only_fields = ['id']


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = ['id']


class ReservationGetSerializer(ReservationSerializer):
    class Meta(ReservationSerializer.Meta):
        fields = '__all__'
        read_only_fields = [
            'id', 'rental', 'checkin', 'checkout'
        ]

