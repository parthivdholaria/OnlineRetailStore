from django.shortcuts import render
from .cart import Cart
from django.shortcuts import get_object_or_404
from retailstore.models import Products
from django.http import JsonResponse

# Create your views here.


def cart_summary(request):

    cart = Cart(request)

    data = {'cart': cart}

    return render(request, 'cart/cart-summary.html', data)


def add_to_cart(request):

    cart = Cart(request)

    if (request.POST.get('action') == 'post'):
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        # checking in the database whether those products match
        product = get_object_or_404(Products, id=product_id)

        cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})

        return response


def delete_from_cart(request):
    
    cart = Cart(request)

    if (request.POST.get('action') == 'post'):
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)

        cart_quantity = cart.__len__()

        cart_total = cart.get_total()

        response = JsonResponse({'qty': cart_quantity,'total':cart_total})

        return response


def update_cart(request):
    
    cart = Cart(request)

    if (request.POST.get('action') == 'post'):

        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        cart.update(product=product_id,qty=product_quantity)

        cart_quantity = cart.__len__()

        cart_total = cart.get_total()

        response = JsonResponse({'qty': cart_quantity,'total':cart_total})

        return response