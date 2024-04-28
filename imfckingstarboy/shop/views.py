from django.shortcuts import render, get_object_or_404
from .models import Book
# Create your views here.


def all_items(request):
    books = Book.objects.all()

    return render(request, 'shop.html', {'books':books}) 

def single_quote(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'single_book.html', {'book': book})