from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Book model.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
