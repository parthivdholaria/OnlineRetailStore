from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.cart_summary,name='cart-summary'),
    path('add/',views.add_to_cart,name='cart-add'),
    path('delete/',views.delete_from_cart,name='cart-delete'),
    path('update/',views.update_cart,name='cart-update'),

]