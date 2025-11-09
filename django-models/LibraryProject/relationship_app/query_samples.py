import os
import django

# Setup Django environment so we can run queries outside manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
def run_queries():
    # 1️⃣ Query all books by a specific author
    author_name = "J.K. Rowling"  # Change to the author you have in DB
    try:
        author = Author.objects.get(name=author_name)
        print(f"Books by {author.name}:")
        for book in author.books.all():
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # 2️⃣ List all books in a library
    library_name = "Central Library"  # Change to your library name
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in library '{library.name}':")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # 3️⃣ Retrieve the librarian for a library
    try:
        print(f"\nLibrarian of library '{library.name}': {library.librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library.name}'")


if __name__ == "__main__":
    run_queries()
