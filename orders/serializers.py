from rest_framework import serializers
from orders.models import Order
from accounts.models import Customer
from books.models import Book

from accounts.serializers import CustomerSerializer
from books.serializers import BookSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    book = BookSerializer()


    class Meta:
        fields = [
            "id",
            "price_per_book",
            "book",
            "customer",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["price_per_book"]

        model = Order

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['book','customer']

