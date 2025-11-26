from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# List all books
# Anyone can read
# Optional filtering by author via query parameter: ?author=1
# -------------------------------
class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.query_params.get('author')
        if author_id:
            queryset = queryset.filter(author__id=author_id)
        return queryset

# -------------------------------
# Retrieve single book by ID
# Anyone can read
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# -------------------------------
# Create a new book
# Only authenticated users can create
# Custom validation: publication_year cannot be in the future
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > 2025:  # Replace with current year if needed
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# -------------------------------
# Update an existing book
# Only authenticated users can update
# Custom validation: publication_year cannot be in the future
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.validated_data['publication_year'] > 2025:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# -------------------------------
# Delete a book
# Only authenticated users can delete
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
