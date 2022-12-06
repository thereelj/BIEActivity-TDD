from rest_framework import serializers

from core.models import Rental


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = '__all__'
        read_only_fields = ['id']
        