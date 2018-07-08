from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Category(models.Model):
    name      = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserDetails(models.Model):
    user_name = models.CharField(max_length=200)
    email     = models.EmailField()
    password  = models.CharField(max_length=100)
    CCName      = models.CharField(max_length=200 ,default ="mmmm")
    Code_Num  = models.IntegerField(default=00000)
    Expiration_date =models.DateTimeField(null=True, blank=True)
    CVC       = models.IntegerField(default=00000)
    city      = models.CharField(max_length=255 , default="Menofia")
    location  = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_Image      = models.ImageField(upload_to ="image" ,blank=True)
    product_name = models.CharField(max_length =300)
    price        = models.PositiveIntegerField()
    Category     = models.ForeignKey("Category" ,on_delete=models.CASCADE,null=True, blank=True)
    view         = models.PositiveIntegerField()
    Start_data   = models.DateTimeField(auto_now_add=True ,null=True, blank=True)
    End_data     = models.DateTimeField(auto_now_add=False,null=True, blank=True )
    def __str__(self):
        return ''.join(self.product_name)


class UserOrder(models.Model):
    user_name    = models.ManyToManyField(UserDetails)
    product_name = models.ManyToManyField(Product)
    Total_price  = models.PositiveIntegerField()

    def display_username(self):
        return ' , '.join([username.user_name for username in self.user_name.all()[:]])
    display_username.short_description = 'USer_Name'

    def display_product(self):
        return ' ,  '.join([product.product_name for product in self.product_name.all()[:]])
    display_product.short_description="Product"
