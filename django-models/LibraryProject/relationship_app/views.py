from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# -----------------------------------------------
# Function-Based View: List all books
# -----------------------------------------------
def list_books(request):
    """
    Displays all books in the database along with their authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# -----------------------------------------------
# Class-Based View: Library details
# -----------------------------------------------
class LibraryDetailView(DetailView):
    """
    Displays details of a specific library and lists all books in it.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
