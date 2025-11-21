from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # <-- add this import
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides CRUD operations for Book model.

    Authentication: Token required
    Permissions: Only authenticated users can access
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
