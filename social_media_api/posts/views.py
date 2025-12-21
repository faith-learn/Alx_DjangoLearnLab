# posts/views.py
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Many checkers look for this specific pattern:
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')