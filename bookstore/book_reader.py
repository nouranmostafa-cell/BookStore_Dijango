import os
from django.conf import settings

def get_all_books():
    books = []
    file_path = os.path.join(settings.BASE_DIR, 'bookstore', 'data', 'books.txt')
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                book_id, title, description, image_path = line.strip().split('|')
                books.append({
                    'id': book_id,
                    'title': title,
                    'description': description,
                    'image_path': image_path
                })
    return books

def get_book_by_id(book_id):
    books = get_all_books()
    for book in books:
        if book['id'] == str(book_id):
            return book
    return None