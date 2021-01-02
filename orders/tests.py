from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Customer
from products.models import Book
from orders.models import Order

class OrderTests(APITestCase):

    def setUp(self):
        pass
     
        
        self.custf test_create_order(self):
        """
        Ensure we can create a new order object.
        """
        data = {'price_per_book': '100'}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().price_per_book, '100')

    def test_get_order_list(self):
        Order.objects.create(name="Test Order", description="test test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

