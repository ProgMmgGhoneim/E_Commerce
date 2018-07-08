from django.contrib import admin
from user.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display  = ['user_name' ,'email','CCName','Code_Num','Expiration_date','CVC','city']
    list_filter   = ['user_name','CCName','CVC','city','Expiration_date']
    search_fields = ['user_name','CCName','CVC','city','Expiration_date']
    fieldsets = (
    ('personal informtion' , {'fields' : ('user_name' ,'email','password') }),
    ('credit card', {'fields': ('CCName','Code_Num','Expiration_date','CVC','city','location')}),
    )

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','Category','view','End_data']
    list_filter  = ['product_name','price','Category','view','End_data']
    search_fields= ['product_name','price','Category','view','End_data']
    fieldsets =(
    ('product INFO' , {'fields' : ('product_Image' ,'product_name','price') }),
    ('Additional INFO' ,{'fields': ('Category','view','End_data')})

    )

class OrderAdmin(admin.ModelAdmin):
    list_display = ['display_username','display_product','Total_price']
    list_filter  = ['Total_price']
    search_fields= ['Total_price']

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter  = ['name']
    search_fields= ['name']



admin.site.register(Product ,ProductAdmin)
admin.site.register(UserDetails,UserAdmin)
admin.site.register(Category ,CategoryAdmin)
admin.site.register(UserOrder,OrderAdmin)
