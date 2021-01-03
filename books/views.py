
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    