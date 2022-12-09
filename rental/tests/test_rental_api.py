from django.test import TestCase
from django.urls import reverse

from core.models import (
    Rental,
    Reservation
)


def reservation_detail_url(rental, reservation_id):

    return reverse('rental:reservation-detail', args=[rental, reservation_id])


def create_rental(**params):
    return Rental.objects.create(**params)


def create_reservation(**params):
    return Reservation.objects.create(**params)


class ReservationAPITests(TestCase):

    @classmethod
    def setUpTestData(cls):
        rental_1 = create_rental(name='rental-1')
        rental_2 = create_rental(name='rental-2')

        # For Rental 1
        create_reservation(rental=rental_1.name, checkin="2022-01-01", checkout="2022-01-13")
        create_reservation(rental=rental_1.name, checkin="2022-01-20", checkout="2022-02-10")
        create_reservation(rental=rental_1.name, checkin="2022-02-20", checkout="2022-03-10")
        # For Rental 2
        create_reservation(rental=rental_2.name, checkin="2022-01-02", checkout="2022-01-20")
        create_reservation(rental=rental_2.name, checkin="2022-01-11", checkout="2022-01-20")

    def test_reservation_1(self):

        reservation_id = 1
        rental = 1
        checkin = '2022-01-01'
        checkout = '2022-01-13'
        previous = '-'
        reservation = {
            'Rental_name': f'rental-{rental}',
            'ID': f'Res-{reservation_id} ID',
            'Checkin': checkin,
            'Checkout': checkout,
            'Previous Reservation, ID': previous
        }
        url = reservation_detail_url(rental, reservation_id)
        res = self.client.get(url)
        self.assertEqual(res.data, reservation)

    def test_reservation_2(self):
        reservation_id = 2
        rental = 1
        checkin = '2022-01-20'
        checkout = '2022-02-10'
        previous = 'Res-1 ID'
        reservation = {
            'Rental_name': f'rental-{rental}',
            'ID': f'Res-{reservation_id} ID',
            'Checkin': checkin,
            'Checkout': checkout,
            'Previous Reservation, ID': previous
        }
        url = reservation_detail_url(rental, reservation_id)
        res = self.client.get(url)
        self.assertEqual(res.data, reservation)

    def test_reservation_3(self):
        reservation_id = 3
        rental = 1
        checkin = '2022-02-20'
        checkout = '2022-03-10'
        previous = 'Res-2 ID'
        reservation = {
            'Rental_name': f'rental-{rental}',
            'ID': f'Res-{reservation_id} ID',
            'Checkin': checkin,
            'Checkout': checkout,
            'Previous Reservation, ID': previous
        }
        url = reservation_detail_url(rental, reservation_id)
        res = self.client.get(url)
        self.assertEqual(res.data, reservation)

    def test_reservation_4(self):
        reservation_id = 4
        rental = 2
        checkin = '2022-01-02'
        checkout = '2022-01-20'
        previous = '-'
        reservation = {
            'Rental_name': f'rental-{rental}',
            'ID': f'Res-{reservation_id} ID',
            'Checkin': checkin,
            'Checkout': checkout,
            'Previous Reservation, ID': previous
        }
        url = reservation_detail_url(rental, reservation_id)
        res = self.client.get(url)
        self.assertEqual(res.data, reservation)

    def test_reservation_5(self):
        reservation_id = 5
        rental = 2
        checkin = '2022-01-11'
        checkout = '2022-01-20'
        previous = 'Res-4 ID'
        reservation = {
            'Rental_name': f'rental-{rental}',
            'ID': f'Res-{reservation_id} ID',
            'Checkin': checkin,
            'Checkout': checkout,
            'Previous Reservation, ID': previous
        }
        url = reservation_detail_url(rental, reservation_id)
        res = self.client.get(url)
        self.assertEqual(res.data, reservation)