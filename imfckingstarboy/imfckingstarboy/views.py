from django.shortcuts import render
from quotes.models import Quote
from shop.models import Book

def home(request):
    quotes = Quote.objects.all().order_by('-id')[:3]
    books = Book.objects.all()
    return render(request, 'home.html',{'quotes':quotes, 'books':books})

def order_confirmation(request):
    return render(request, 'order_confirmation.html')