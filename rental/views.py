from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from core.models import Rental
from rental import serializers


class RentalAPIView(ListCreateAPIView):
    serializer_class = serializers.RentalSerializer
    queryset = Rental.objects.all()

    def get_queryset(self):
        return Rental.objects.all().order_by('-id')


class RentalDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RentalSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Rental.objects.filter(id=self.kwargs.get('id'))
