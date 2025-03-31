# RaD-GP-C25-P-G1: Library Management System
> **Python - Building a Library Management System using Python and Object-Oriented Programming**  

---

## Overview

This project is a **command-line-based Library Management System** developed as part of a coursework assignment to assess practical knowledge in:
- Python programming
- Object-Oriented Design (OOD)
- Modular architecture
- Testing and code quality best practices

The system allows users to manage a library's book collection, including borrowing and returning functionality, while applying key software engineering principles like encapsulation, separation of concerns, and exception handling.

---

##  Project Goals

- Demonstrate the use of Python classes for modeling real-world entities (`Book`, `Author`, `Library`)
- Implement a fully functional library system using Object-Oriented Programming
- Adhere to industry practices including modular design, PEP 8, exception handling, and test coverage

---

##  Features Implemented

- Add, remove, borrow, return, and list books
- Search books by title or author
- Relationships: Authors can have multiple books, a library manages many books
- Unit tests with structured coverage (~80–90%)
- JSON-based persistent storage
-  Simple and interactive CLI menu

---

## Technologies & Resources

- Python 3.12+
- `unittest` for testing
- JSON for file persistence

### Learning Materials:
- [Python Full Course – YouTube](https://youtu.be/ix9cRaBkVe0?si=lU2X6nRVVqqKMN6-)

---

## Project Structure

```bash
library_management_system/
├── main.py                  # Application entry point
├── models/                  # Core class definitions
│   ├── book.py
│   ├── author.py
│   └── library.py
├── services/                # Business logic and storage
│   ├── manager.py
│   └── storage.py
├── ui/                      # CLI interface
│   └── cli.py
├── exceptions/              # Custom exception classes
│   └── errors.py
├── tests/                   # Unit tests
│   ├── test_book.py
│   ├── test_author.py
│   ├── test_library.py
│   └── test_manager.py
├── data/
│   └── data.json            # JSON file for persistence
└── README.md
