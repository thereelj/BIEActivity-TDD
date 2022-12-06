from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Rental

from rental.serializers import RentalSerializer

RENTAL_URL = reverse('rental:rental-list')


def create_rental(**params):
    """Create and return a sample reservation"""
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

        res = self.client.get(RENTAL_URL)

        rentals = Rental.objects.all().order_by('id')
        serializer = RentalSerializer(rentals, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
