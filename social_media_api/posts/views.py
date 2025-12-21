from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Use pk to get the specific post
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Check if already liked, otherwise create
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification for the post author
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post,
                    target_content_type=ContentType.objects.get_for_model(post),
                    target_object_id=post.id
                )
            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        return Response({"error": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"error": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)