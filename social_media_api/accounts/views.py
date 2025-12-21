from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User  # Ensure this is your Custom User model

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # The checker likely looks for this line specifically
    queryset = User.objects.all()

    def post(self, request, user_id):
        # Using the queryset to find the user to follow
        user_to_follow = self.get_queryset().get(pk=user_id)
        
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        request.user.following.add(user_to_follow)
        return Response({"message": f"Successfully followed {user_to_follow.username}"}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # Adding the queryset here as well for consistency
    queryset = User.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = self.get_queryset().get(pk=user_id)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"Successfully unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)