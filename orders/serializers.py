from rest_framework import serializers
from orders.models import Order
from accounts.serializers import CustomerSerializer
from books.serializers import BookSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    book = BookSerializer()


    class Meta:
        fields = ['id','price_per_book','book','customer',"created_at","updated_at"]
        read_only_fields = ['price_per_book']

        model = Order

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order 
        fields = ['id','price_per_book','book','customer',"created_at","updated_at"]
        read_only_fields = ['price_per_book']
    
    def create(self, validated_data):
        book = Book.objects.get(pk=validated_data["book"])
        customer = Customer.objects.get(pk=validated_data["customer"])
        order = Order.objects.create(
                book=book, customer=customer
            )
        order.save()
        return order


