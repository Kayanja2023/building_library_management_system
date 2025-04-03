import os                                       # importing the os module
import json                                     # importing the json module
from models.book import Book

""" Load books from JSON file and return a list of Book objects"""
def load_books(filepath):
    if not os.path.exists(filepath):            # checks if the file exists
        return []

    with open(filepath, "r") as f:              # opens and reads the file
        content = f.read()
        if not content.strip():                 # If the file is empty or only contains whitespace, return an empty list
            return []

        try:
            data = json.loads(content)          # parse JSON data and reconstruct Book instances
            return [Book.from_dict(entry) for entry in data]
        except json.JSONDecodeError:
            print(f"Warning: Failed to decode JSON from {filepath}")
            return []                           # return an empty list as fallback


""" saving a list of Book objects to a JSON file"""
def save_books(filepath, books):
    with open(filepath, 'w') as f:              # serialize each Book to a dictionary and write to the file
        json.dump([b.to_dict() for b in books], f, indent=2)