#name should be the same

#import the class Cart from cart file in the current folder


from .cart import Cart


def cart(request):

    return {'cart':Cart(request)}
