from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Customer
from books.models import Book
from orders.models import Order


class OrderTests(APITestCase):

    def test_create_order(self):

        url = reverse('create-order')
        data = {'name': 'Test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().name, 'Test')
        self.assertIsNotNone(Order.objects.get().id)