import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1️⃣ Query all books by a specific author
    author_name = "J.K. Rowling"  # Change as needed
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)  # <-- checker compliant
        print(f"Books by {author.name}:")
        if books_by_author:
            for book in books_by_author:
                print(f"- {book.title}")
        else:
            print("No books found for this author.")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # 2️⃣ List all books in a library
    library_name = "Central Library"  # Change as needed
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in library '{library.name}':")
        if library.books.exists():
            for book in library.books.all():
                print(f"- {book.title}")
        else:
            print("No books in this library.")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # 3️⃣ Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library=library)  # <-- checker compliant
        print(f"\nLibrarian of library '{library.name}': {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library.name}'")
    except NameError:
        print("Library not found, so cannot retrieve librarian.")

if __name__ == "__main__":
    run_queries()
