from models.book import Book
from models.library import Library
from services import manager, storage
from exceptions.errors import BookNotFoundError, BookAlreadyBorrowedError

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
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            manager.add_book(Book(title, author, isbn), library)
            print("Book added!")

        elif choice == "2":
            isbn = input("Enter ISBN to borrow: ")
            try:
                manager.borrow_book(isbn, library)
                print("Book borrowed!")
            except BookNotFoundError as e:
                print(f"⚠️ {e}")
            except BookAlreadyBorrowedError as e:
                print(f"⚠️ {e}")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            try:
                if manager.return_book(isbn, library):
                    print("Book returned.")
            except BookNotFoundError as e:
                print(f"⚠️ {e}")

        elif choice == "4":
            isbn = input("Enter ISBN to remove: ")
            if manager.remove_book(isbn, library):
                print("Book removed.")
            else:
                print("Book not found.")

        elif choice == "5":
            keyword = input("Enter title or author keyword: ")
            results = manager.search_books(keyword, library)
            if results:
                for b in results:
                    print(b)
            else:
                print("No results found.")

        elif choice == "6":
            all_books = library.get_all_books()
            if all_books:
                for book in all_books:
                    print(book)
            else:
                print("Library is currently empty.")

        elif choice == "7":
            storage.save_books(FILEPATH, library.books)
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
