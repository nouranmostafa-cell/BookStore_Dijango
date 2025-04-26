from django.shortcuts import render, get_object_or_404
from .book_reader import get_all_books, get_book_by_id
from .models import Author
from .models import Book



def book_list(request):
    #books = get_all_books()
    books = Book.objects.all() 
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not book:
        return render(request, 'bookstore/404.html', status=404)
    return render(request, 'bookstore/book_detail.html', {'book': book})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()  
    
    return render(request, 'bookstore/author_detail.html', {
        'author': author,
        'books': books
    })
