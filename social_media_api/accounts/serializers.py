from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Use get_user_model() as requested by the task
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    # Explicitly using serializers.CharField for the password check
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio')

    def create(self, validated_data):
        # Using get_user_model().objects.create_user as requested
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user