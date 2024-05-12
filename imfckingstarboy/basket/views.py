from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render


from .models import Order
from shop.models import Book

from .basket import Basket

from .forms import CheckoutForm


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Book, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
    

def checkout(request):
    print("CHEKOUT FORM")
    
    basket = Basket(request)

    print(basket.get_total_price())
    ordered_items = basket.basket_content()
    print(basket.basket_content())

    if request.method== "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                city = form.cleaned_data['city'],
                post_code = form.cleaned_data['post_code'],
                phone_number = form.cleaned_data['phone_number'],
                price = basket.get_total_price(),
                items = ordered_items

            )
    else:
        initial_data = {
            'items': ordered_items
        }
        form = CheckoutForm(initial=initial_data)
    return render(request, 'checkout.html', {'form': form})
    

    