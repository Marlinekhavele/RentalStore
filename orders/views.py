from rest_framework import generics
from rest_framework.response import Response
from django_filters import rest_framework as filters
from orders.models import Order
from orders.serializers import (
    OrderSerializer,
    OrderCreateSerializer
)

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        create_serializer = OrderSerializer(order)
        return Response(create_serializer.data)

class ListOrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('customer__id',)
