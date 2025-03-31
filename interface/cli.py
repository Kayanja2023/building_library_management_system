from models.book import Book
from models.library import Library
from services import manager, storage

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
            if manager.borrow_book(isbn, library):
                print("Book borrowed!")
            else:
                print("Not available or not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            if manager.return_book(isbn, library):
                print("Book returned.")
            else:
                print("Book not found.")

        elif choice == "4":
            isbn = input("Enter ISBN to remove: ")
            if manager.remove_book(isbn, library):
                print("Book removed.")
            else:
                print("Book not found.")

        elif choice == "5":
            keyword = input("Enter title or author keyword: ")
            results = manager.search_books(keyword, library)
            for b in results:
                print(b)

        elif choice == "6":
            for book in library.get_all_books():
                print(book)

        elif choice == "7":
            storage.save_books(FILEPATH, library.books)
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")