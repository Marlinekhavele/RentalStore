
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import  Book

class BookTests(APITestCase):

    def test_create_Book(self):
        url = reverse("book-list")
        data = {
            "title": "Home Deus",
            "isbn": "9780062464316",
            "author": "Yuval Noah",
            "pages": 464,
            "publisher": "Harper; Illustrated edition (February 21, 2017)",
        }
        response = self.client.post(url, data, format="json")
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Home Deus")
        self.assertIsNotNone(Book.objects.get().book_type)
        self.assertEqual(response_json["book_type"],"regular")
        self.assertEqual(response_json["daily_charge"],1.50)
        self.assertIsNotNone(Book.objects.get().daily_charge)
        self.assertIsNotNone(Book.objects.get().id)