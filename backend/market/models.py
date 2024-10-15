import uuid
from django.db import models
from Django.core.validators import RegexValidator


# Customer Models

class Customer(models.Model):
    id = models.UUIDField(primary_key = True, unique = True, default = uuid.uuid4)
    
    first_name = models.CharField(max_length = 50)
    
    last_name = models.Charfield(max_length = 50)
    
    phone_number = models.CharField(validators =[RegexValidator (regex = r'^\d{11}$')],max_length = 11, blank = True)
    
    email = models.EmailField(unique = True)
    
    address = models.TextField()
    
    date_joined = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
      return self.first_name
      
 
      
                
# Product Models 


class Product (models.Model):
    id = models.UUIDField(primary_key = True, unique = True, default = uuid.uuid4)
    
    name = models.CharField(max_length = 50)
    
    description = models.TextField()
    
    price = models.DecimalField(max_length = 10, decimal_places = 2)
    
    category = models.CharField(max_length = 50 )
    
    stock_quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.name}-{self.price}"

  
    
        
     
# sales Models

class Sale (models.Model):
    id = models.UUIDField(primary_key = True, unique = True, default = uuid.uuid4)
    
    customer = Models.ForeignKey(Customer,on_delete = models.CASCADE,null = True)
    
    product = models.ForeignKey(Product,on_delete = models.CASCADE,null = True)
    
    sale_date = models.DateTimeField(auto_now_add = True)
    
    sale_amount = models.DecimalField(max_length = 10,decimal_places = 2)
    
    def __str__(self):
        return f"{self.product}-{self.sale_amount}"
 
  
       
            
                      
#Market_Trend Models
class Market_Trend(models.Model):
         
         id = models.UUIDField(primary_key = True, unique = True, default = uuid.uuid4)
         
         trend_name = models.CharField(max_length = 50)
         
         trend_type = models.CharField(max_length = 20)
         
         description = models.TextField()
         
         start_date = models.DateTimeField()
         
         end_date = models.DateTimeField()
         
         def __str__(self):
             return self.trend_name
         
    