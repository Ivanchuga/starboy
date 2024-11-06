from django.shortcuts import render, get_object_or_404
from .models import Book
from django.urls import reverse
# Create your views here.


def all_items(request):
    books = Book.objects.all().order_by('-id')

    return render(request, 'shop.html', {'books':books}) 

def single_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'single_book.html', {'book': book})

#def get_absolute_url(self):
#        #return reverse('store:product_detail', args=[self.slug])
#        print("GET ABSOLUTE URL")
#        return reverse('single_book', args=[str(self.id)])