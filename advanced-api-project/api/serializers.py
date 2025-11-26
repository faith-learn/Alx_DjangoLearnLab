# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields.
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id']

    def validate_publication_year(self, value):
        """
        Ensure publication_year is not greater than current year.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year ({value}) cannot be in the future (current year {current_year})."
            )
        return value

class AuthorBookSerializer(serializers.ModelSerializer):
    """
    Small serializer to use for nested representation (optional).
    We could reuse BookSerializer, but this avoids circular writes if you want
    separate behavior for nested read.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author with a nested list of their books.
    The nested `books` field comes from the related_name='books' on the FK.
    """
    books = AuthorBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        read_only_fields = ['id']
