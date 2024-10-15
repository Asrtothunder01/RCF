from django.contrib import admin

from .models import Customer,Product,Sale,Market_Trend



@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
 list_display = ('first_name','last_name','email')
 
 search_fields = ['first_name','email']
 
  
   
     
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
 list_display = ('name','price')
 
 search_fields = ['name','price__category']
 
 
 
@admin.register(Sale)

class SaleAdmin(admin.ModelAdmin):
 list_display = ('customer','product','sale_amount')
 
 search_fields = ['customer','product__sale_amount']
 
 
@admin.register(Market_Trend)

class Market_Trend(admin.ModelAdmin):
    list_display = ('trend_name','trend_type','start_date')
    
    search_fields = ['trend_name','trend_type__start_date']