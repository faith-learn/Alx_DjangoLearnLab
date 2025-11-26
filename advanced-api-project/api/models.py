# api/models.py
from django.db import models

class Author(models.Model):
    """
    Represents an author. One Author can have many Book objects (one-to-many).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book. Each Book references an Author (ForeignKey).
    The publication_year is stored as an integer (e.g., 2023).
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # allows author.books to access related Book objects
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
