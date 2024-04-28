from django.shortcuts import render, get_object_or_404
from .models import Quote

# Create your views here.

def all_quotes(request):
    quotes = Quote.objects.all()

    return render(request, 'all_quotes.html', {'quotes': quotes})

def latest_quotes(request):
    quotes = Quote.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'latest_quotes': quotes})

def single_quote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)

    return render(request, 'single_quote.html', {'quote': quote})