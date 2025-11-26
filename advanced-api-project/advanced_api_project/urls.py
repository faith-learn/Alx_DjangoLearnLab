"""
URL configuration for advanced_api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Retrieve a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # Update an existing book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    
    # Delete a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
