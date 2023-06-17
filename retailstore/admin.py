from django.contrib import admin

from .models import Categories,Products

# Register your models here.

#Method-1
# admin.site.register(Categories)
# admin.site.register(Products)


#method2

@admin.register(Categories)
class AdminCategory(admin.ModelAdmin) :
    prepopulated_fields = {'slug':('name',)}


@admin.register(Products)
class ProductsCategory(admin.ModelAdmin) :
    prepopulated_fields = {'slug':('name',)}