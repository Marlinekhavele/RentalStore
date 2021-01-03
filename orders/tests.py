from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Customer
from books.models import Book
from orders.models import Order



class OrderTests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            isbn="978-1524763138",
            title="Becoming",
            publisher="Crown; 1st Edition (November 13, 2018)",
            author="Michelle Obama",
            pages=400,
        )
        self.customer = Customer.objects.create(
            username="customer_one",
            password="customer_password",
        )

    def test_create_order(self):
        url = reverse("create-order")
        data = {"book": self.book.id, "customer": self.customer.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().price_per_book, 1.00)
        self.assertIsNotNone(Order.objects.get().id) 