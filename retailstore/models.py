from django.db import models

from django.urls import reverse

# Create your models here.


# This is the place where we create classes for diffrent objects for our store
# first would be categories: eg--> electronics shoes dairy etc... 

class Categories(models.Model) :

    name = models.CharField(max_length=100,db_index=True)  #here db_index is used for query accelaration and faster memory access

    slug = models.SlugField(max_length=100,unique=True)   #used for selecting a particular category which is unique

    #define a class meta because by default Objects are appended with the name S  to avoid we give our own name
    class Meta:
        verbose_name_plural = 'categories'

    
    #overriding the toString function
    def __str__(self) :

        return f'{self.name}'
    
    def get_absolute_url(self):

        return reverse("list-category",args={self.slug})

    

class Products(models.Model):

    category = models.ForeignKey(Categories, related_name='product', on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=9,decimal_places=2)

    description = models.TextField(blank=True)  #blank implies optional

    slug = models.SlugField(max_length=100,unique=True)

    brand =models.CharField(max_length=100,default='unbranded')

    image = models.ImageField(upload_to='images/',default="")


    #define a class meta because by default Objects are appended with the name S  to avoid we give our own name
    class Meta:
        verbose_name_plural = 'products'

    
    #overriding the toString function
    def __str__(self) :

        return f'{self.name}'


    def get_absolute_url(self):
        return reverse("product-info",args={self.slug})

    
    



