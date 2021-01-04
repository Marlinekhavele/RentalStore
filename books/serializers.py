from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','isbn','title','publisher','book_type','daily_charge','author','pages']
        model = Book