from rest_framework import serializers
from orders.models import Order
from accounts.serializers import CustomerSerializer
from books.serializers import BookSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    book = BookSerializer()


    class Meta:
        fields = ['id','price','book','customer',"created_at","updated_at",]
        model = Order

      