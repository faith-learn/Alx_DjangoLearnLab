from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView # Add FeedView here

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user_feed'), # Feed goes BEFORE router.urls usually
    path('', include(router.urls)),
]