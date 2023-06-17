from django.shortcuts import render

from .models import Categories,Products

from django.shortcuts import get_object_or_404

# Create your views here.


def retailstore(request) :

    # run a select query and make a dictionary and modify the return statement

    products = Products.objects.all()

    data = {'products':products}

    return render(request,'retailstore/retailstore.html',data)


def categories(request):


    # run a select query and make a dictionary and modify the return statement

    categories = Categories.objects.all()  #returns a json object

    return {'categories':categories}

    


def product_info(request,product_slug):

    #basically from the Prodcut table search the tuples where slug entered matches the product slug
    #run the select + where query here 

    product = get_object_or_404(Products,slug=product_slug)

    data = {'product':product}

    return render(request,'retailstore/product-info.html',data)



def list_category(request,category_slug=None):

    # run again the select category from category table

    #select products based on the 
    
    category = get_object_or_404(Categories,slug = category_slug)

    products = Products.objects.filter(category=category)

    return render(request,"retailstore/list-category.html",{'category':category,'products':products})

