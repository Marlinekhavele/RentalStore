from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from orders.models import Order
from orders.serializers import OrderSerializer

class OrderViewSet(viewsets.ViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    

    