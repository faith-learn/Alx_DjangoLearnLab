from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create a post model.
class Post(models.Model):
    title= models.CharField(max_length=50)
    content= models.TextField(max_length=200)
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = TaggableManager()
    

def _str_(self):
        return self.title



#implementing a comment functionality
class Comment(models.Model):
      post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)
      author=models.ForeignKey(User,on_delete=models.CASCADE)
      content=models.TextField()
      created_at=models.DateTimeField(default=timezone.now)
      updated_at=models.DateTimeField(auto_now=True)
def _str_(self):
    return f"Comment by {self.author} on {self.post}"
#implementing tag model functionality
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tags = models.ManyToManyField(Post, related_name='posts', blank=True)

def _str_(self):
        return self.name
#modify post model