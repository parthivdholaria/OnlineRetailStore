from decimal import Decimal
from retailstore.models import Products


class Cart():

    def __init__(self, request):

        # check if the cart is already filled then show that cart
        # else assign an empty cart to the new user

        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

        # to see this working
        # python manage.py shell

        # from django.contrib.sessions.models import Sessions

        # s_key = Session.objects.get(pk='key form the developper tools under cookies')
        # s_key.get_decoded

    def add(self, product, product_qty):

        product_id = str(product.id)

        if (product_id in self.cart):

            self.cart[product_id]['qty'] = product_qty

        else:

            self.cart[product_id] = {'price': str(
                product.price), 'qty': product_qty}

        self.session.modified = True

    def delete(self, product):

        product_id = str(product)

        if (product_id in self.cart):
            del self.cart[product_id]

        self.session.modified = True

    def update(self, product, qty):

        product_id = str(product)

        product_quantity = qty

        if (product_id in self.cart):

            self.cart[product_id]['qty'] = product_quantity

        self.session.modified = True

    def __len__(self):

        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):

        all_product_ids = self.cart.keys()

        # loop through database and and check whether the cart products are there in database
        products = Products.objects.filter(id__in=all_product_ids)

        # shallow copy
        # cart = self.cart.copy()

        # deep copy
        import copy
        cart = copy.deepcopy(self.cart)

        for product in products:

            cart[str(product.id)]['product'] = product

        for item in cart.values():

            item['price'] = Decimal(item['price'])

            item['total'] = item['price'] * item['qty']

            yield item

    def get_total(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.cart.values())
