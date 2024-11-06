from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST

from django.contrib import messages


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
    
#@require_POST
def checkout(request):
    print("CHEKOUT FORM")
    
    basket = Basket(request)

    total_price = basket.get_total_price()
    print(type(basket.get_total_price()))
    ordered_items = basket.basket_content()
    print(basket.basket_content())
    
    form = CheckoutForm(request.POST)
    initial_data = {
        'items': ordered_items,
        'price': basket.get_total_price()
    }
    if form.is_valid():
        print("THE FORM IS VALID")
        order = Order.objects.create(
            full_name=form.cleaned_data['full_name'],
            address=form.cleaned_data['address'],
            city = form.cleaned_data['city'],
            post_code = form.cleaned_data['post_code'],
            phone_number = form.cleaned_data['phone_number'],
            price = total_price,
            items = ordered_items,
            
        )
        #form.save()
        print("SACUVANO")
        basket.empty_basket()
        messages.success(request, "Vasa porudzbina je uspesno kreirana")
        
        return redirect('home')
    else:
        
        form = CheckoutForm(initial=initial_data)
        print("FORM IS NOT VALID")
        return render(request, 'checkout.html', {'form': form})
'''
    if request.method == "POST":
        print("REQUEST METHOD POST")
        form = CheckoutForm(request.POST)
        if form.is_valid():
            print("THE FORM IS VALID")
            order = Order.objects.create(
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                city = form.cleaned_data['city'],
                post_code = form.cleaned_data['post_code'],
                phone_number = form.cleaned_data['phone_number'],
                price = basket.get_total_price(),
                items = ordered_items,
                
            )
            form.save()
            
    else:
        initial_data = {
            'items': ordered_items
        }
        form = CheckoutForm(initial=initial_data)
    return render(request, 'checkout.html', {'form': form})
'''

    