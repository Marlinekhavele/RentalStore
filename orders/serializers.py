from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','price','book','customer',"created_at","updated_at",]
        model = Order

      