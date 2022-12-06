from rest_framework import serializers

from core.models import Rental


class RentalSerializer(serializers.ModelSerializer):
    """Serializer for rentals"""
    class Meta:
        model = Rental
        fields = '__all__'
        read_only_fields = ['id']
