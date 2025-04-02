from models.book import Book
from models.library import Library
from services import manager, storage
from exceptions.errors import BookNotFoundError, BookAlreadyBorrowedError, InvalidISBNError

FILEPATH = "data/data.json"

def run_cli():
    library = Library()
    library.books = storage.load_books(FILEPATH)

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Remove Book")
        print("5. Search Books")
        print("6. List All Books")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n[ Add a New Book ]")

            # Re-prompt for a valid title
            while True:
                title = input("Title: ")
                if title.strip():
                    break
                print("[Invalid Title] Title cannot be empty.")

            # Re-prompt for a valid author
            while True:
                author = input("Author: ")
                if author.strip():
                    break
                print("[Invalid Author] Author cannot be empty.")

            # Re-prompt for a valid ISBN using your validation logic
            while True:
                isbn = input("ISBN (13 or 15 digits, numeric only): ")
                try:
                    new_book = Book(title, author, isbn)
                    break  # Success
                except InvalidISBNError as e:
                    print(f"[Invalid ISBN] {e}. Please try again.")

            manager.add_book(new_book, library)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to borrow: ")
            try:
                manager.borrow_book(isbn, library)
                print("Book borrowed!")
            except BookNotFoundError as e:
                print(f" {e}")
            except BookAlreadyBorrowedError as e:
                print(f" {e}")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            try:
                if manager.return_book(isbn, library):
                    print(" Book returned.")
            except BookNotFoundError as e:
                print(f" {e}")

        elif choice == "4":
            isbn = input("Enter ISBN to remove: ")
            if manager.remove_book(isbn, library):
                print(" Book removed.")
            else:
                print(" Book not found.")

        elif choice == "5":
            keyword = input("Enter title or author keyword: ")
            results = manager.search_books(keyword, library)
            if results:
                for b in results:
                    print(b)
            else:
                print(" No results found.")

        elif choice == "6":
            all_books = library.get_all_books()
            if all_books:
                for book in all_books:
                    print(book)
            else:
                print(" Library is currently empty.")

        elif choice == "7":
            storage.save_books(FILEPATH, library.books)
            print(" Library saved. Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
