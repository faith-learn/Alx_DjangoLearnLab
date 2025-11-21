from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList  # your old ListAPIView

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Keep your previous list view if needed
    path('books/', BookList.as_view(), name='book-list'),

    # Include all routes from the router (CRUD operations)
    path('', include(router.urls)),
]
