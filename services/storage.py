import os
import json


from models.book import Book

def load_books(filepath):

    if not os.path.exists(filepath):
        return []

    with open(filepath, "r") as f:
        content = f.read()
        if not content.strip():
            return []

        try:
            data = json.loads(content)
            return [Book.from_dict(entry) for entry in data]
        except json.JSONDecodeError:
            print(f"Warning: Failed to decode JSON from {filepath}")
            return []



def save_books(filepath, books):
    with open(filepath, 'w') as f:
        json.dump([b.to_dict() for b in books], f, indent=2)