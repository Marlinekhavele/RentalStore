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
        self.book_two = Book.objects.create(
            isbn="978-0593236666",
            title="Reflections on the Last Words of Jesus",
            publisher="Convergent Books; Illustrated edition (February 18, 2020)",
            author="Jon Meacham",
            book_type="fiction",
            pages=144
        )
        self.customer = Customer.objects.create(
            username="customer_one",
            password="customer_password",
        )

    def test_create_order(self):
        url = reverse("create-order")
        data = {"book": self.book.id, "customer": self.customer.id}
        response = self.client.post(url, data, format="json")
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertIsNotNone(Order.objects.get().current_charge)
        self.assertIsNotNone(Order.objects.get().id) 

    def test_book_types_have_different_prices(self):
        order_one = Order.objects.create(
            book =  self.book,
            customer = self.customer
        )
        order_two = Order.objects.create(
            book=self.book_two,
            customer=self.customer
        )

        self.assertNotEquals(order_one.current_charge, order_two.current_charge)

    def test_book_altered_prices(self):
        order_one = Order.objects.create(
            book =  self.book,
            customer = self.customer
        )
        order_two = Order.objects.create(
            book=self.book_two,
            customer=self.customer
        )

        self.assertNotEquals(order_one.altered_prices, order_two.altered_prices)
