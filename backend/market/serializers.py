from rest_framework import serializers

from .models import Customer, Product, Sale, Market_Trend


# Serializer

''' CustomerSerializer'''

PHONE_REGEX = r'^\d{11}$'

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Customer
        
        fields = ['id','firstname','lastname','phone_number','email','address','date_joined']
        
        read_only_fields = ['id','date_joined']
        
# Validation For Phone Number
        def validate_phone_number(self, value):
            if not re.match(PHONE_REGEX, value):
                raise serializers.ValidationError('Invalid Phone Number')
            return value
            
# Validation For Email        
        def validate_email(self, value):
            if not re.match(EMAIL_REGEX, value):
                raise serializers.ValidationError('invalid email')
            return value
        

''' ProductSerializer'''  
               
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        
        fields = ['id','name','description','price','category','stock_quantity']
        
        def validate_price(self, value):
            if not value:
                raise serializers.ValidationError('price is required')
            return value
            
        

''' SaleSerializer '''

class SaleSerializer(serializers.ModelSerializer):
    
    customer = CustomerSerializer(read_only = True)
    
    product = ProductSerializer(read_only = True)
 
#Validation of Product       
    def validate_product(sale, value):
        if value is None:
            raise serializers.ValidationError('Product is required')
        if not product.objects.filter(id=('link unavailable')).exists():
            raise serializers.ValidationError('product does not exists')
        return value

# Sale Validation
    def  validate_sale_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('sale amount must be greater than zero')
            
    class Meta:
        
        model = Sale
        
        fields =['id','customer','product','sale_date','sale_amount']
  
    
            
''' Market_Trend  Serializer'''                   
        
class Market_TrendSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Market_Trend
        
        fields = ['id','trend_name','trend_type','description','start_date','end_date']
        
        