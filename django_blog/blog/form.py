from django import forms
from .models import Post,Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Comment
from taggit.forms import TagWidget
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#creating a profile update form

class UpdateUserForm(UserChangeForm):
    password = None  # Hide password field

    class Meta:
        model = User
        fields = ["username", "email"]


#creating comment form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }
#updating post forms for tags


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate tags with commas")

    class Meta:
        model = Post
        fields = ["title","content", 'tags']

    def save(self, commit=True):
        # Save Post object first
        post = super().save(commit=False)

        if commit:
            post.save()

        # Set tags
        tags_input = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_input.split(',') if t.strip()]

        # TaggableManager has built-in set method that handles creation
        post.tags.set(*[tag_names])  # <-- This automatically creates and assigns tags

        return post





#creating a post form

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Add tags separated by commas'}),
        }