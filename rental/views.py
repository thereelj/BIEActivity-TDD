from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import status
from rest_framework.response import Response

from core.models import Rental, Reservation
from rental import serializers


def get_previous_reservation(obj):
    reservation_id = obj.reservation_id
    rental = obj.rental
    previous_reservation = Reservation.objects.filter(reservation_id=reservation_id-1).first()
    if not previous_reservation:
        if previous_reservation.rental == rental:
            if reservation_id > 1:
                order = reservation_id - 1
                prev_res_id = f'Res-{order} ID'
                return prev_res_id
    return '-'


def get_response_data(obj):
    prev_res_id = get_previous_reservation(obj)
    data = {
            'Rental_name': obj.rental,
            'ID': f'Res-{obj.reservation_id} ID',
            'Checkin': str(obj.checkin),
            'Checkout': str(obj.checkout),
            'Previous Reservation, ID': prev_res_id
        }
    return data


class RentalAPIView(ListCreateAPIView):
    serializer_class = serializers.RentalSerializer

    def get_queryset(self):
        return Rental.objects.all().order_by('-rental_id')


class RentalDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.RentalSerializer
    lookup_field = 'rental_id'

    def get_queryset(self):
        return Rental.objects.filter(rental_id=self.kwargs.get('rental_id'))


class ReservationAPIView(ListCreateAPIView):
    serializer_class = serializers.ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(rental='rental-1').order_by('-reservation_id')
        # return Reservation.objects.filter(rental=f"rental-{self.kwargs.get('rental_id')}").order_by('-reservation_id')


class ReservationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ReservationGetSerializer
    lookup_field = 'reservation_id'

    def get(self, request, *args, **kwargs):
        obj = Reservation.objects.get(reservation_id=self.kwargs.get('reservation_id'),
                                      rental=f"rental-{self.kwargs.get('rental_id')}")
        return Response(get_response_data(obj), status=status.HTTP_200_OK)

    def get_queryset(self):
        return Reservation.objects.filter(reservation_id=self.kwargs.get('reservation_id'),
                                          rental=f"rental-{self.kwargs.get('rental_id')}")

