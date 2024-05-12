from django.shortcuts import render, redirect


from shop.models import Book
# Create your views here.


def checkout(request):
    if request.method == "POST":

        for item in request.session['cart']:
            product_id = item['product_id']
            quantity_ordered = item['qty']
            product = Book.objects.all(id=product_id)
            product.quantity -= quantity_ordered
            product.save()
        
        return redirect('order_confirmation')

    return render(request, 'checkout.html')
