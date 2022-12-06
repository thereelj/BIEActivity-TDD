from rest_framework.generics import ListCreateAPIView

from core.models import Rental
from rental import serializers


class RentalAPIView(ListCreateAPIView):
    serializer_class = serializers.RentalSerializer
    queryset = Rental.objects.all()

    def get_queryset(self):
        return Rental.objects.all()
