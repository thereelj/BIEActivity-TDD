from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Rental

from rental.serializers import (
    RentalSerializer,
    # RentalDetailSerializer
)

RENTAL_URL = reverse('rental:rental-list')


def detail_url(rental_id):
    """Create and return a rental detail URL"""
    return reverse('rental:rental-detail', args=[rental_id])


def create_rental(**params):
    """Create and return a sample rental"""
    defaults = {
        'name': 'rental-1',
    }
    defaults.update(params)

    rental = Rental.objects.create(**defaults)
    return rental


class RentalAPITests(TestCase):

    def test_retrieve_rentals(self):
        """Test retrieving the list of rentals."""
        create_rental()
        create_rental(name='rental-2')
        print(RENTAL_URL)
        res = self.client.get(RENTAL_URL)

        rentals = Rental.objects.all().order_by('-id')
        serializer = RentalSerializer(rentals, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_rental_detail(self):
        """Test get rental detail"""
        rental = create_rental()
        url = detail_url(rental.id)
        res = self.client.get(url)

        serializer = RentalSerializer(rental)
        print('res', res.data)
        print('serializer', serializer.data)
        self.assertEqual(res.data, serializer.data)
