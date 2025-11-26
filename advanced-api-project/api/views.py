# api/views.py
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import AllowAny  # or change to IsAuthenticated

class AuthorViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD for Author. Nested books are provided in the AuthorSerializer.
    """
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class BookViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD for Book. BookSerializer includes validation for publication_year.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
