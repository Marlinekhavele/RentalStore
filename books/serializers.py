from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','isbn','title','publisher','author','pages',"created_at","updated_at",]
        model = Book