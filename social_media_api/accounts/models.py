from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='followers', 
        blank=True
    )
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)