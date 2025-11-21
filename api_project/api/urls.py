from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create router and register BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# Include all router URLs
urlpatterns = [
    path('', include(router.urls)),
]
