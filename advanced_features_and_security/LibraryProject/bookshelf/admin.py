# bookshelf/admin.py
from django.contrib import admin
from .models import Book
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ("title", "author", "publication_year")

    # Add a search box for quick lookups by title or author
    search_fields = ("title", "author")

    # Filter sidebar to narrow down by publication year
    list_filter = ("publication_year",)

    # Optional UX improvements
    ordering = ("-publication_year", "title")
    list_per_page = 25