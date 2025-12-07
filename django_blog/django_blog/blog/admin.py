from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    list_filter = ('status', 'author')
    search_fields = ('title', 'content')
    ordering = ('-published_date',)
