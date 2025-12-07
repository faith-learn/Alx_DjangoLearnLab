from django.urls import path
from .views import PostListView,PostDetailView,PostDeleteView,PostCreateView,PostUpdateView
from django.contrib.auth import views as auth_views
from . import views
from .views import  CommentUpdateView, CommentDeleteView,CommentCreateView,search_posts, posts_by_tag
urlpatterns=[ 
path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),]