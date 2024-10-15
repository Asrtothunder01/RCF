from rest_framework.generics import ListAPIView, CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import Customer,Sale,Product, Market_Trend

from .serializers import CustomerSerializer, ProductSerializer, Market_TrendSerializer, SaleSerializer

from rest_framework.exceptions import APIEXCEPTION

from drf_spectacular.utils import extend_schema


# My Views


'''CUSTOMER VIEW'''

# Custom View

@extend_schema(
  tags = ['Customer'],
  
  responses = {200: CustomerSerializer (many = True)},

)
class CustomerListView(ListAPIView):
    
    queryset = Customer.objects.all()
    
    serializer_class = CustomerSerializer
    
    permission_classes =[IsAuthenticated]
    
    pagination_class = None
 
 
 
@extend_schema(
  tags = ['Customer'],
  
  responses = {201: CustomerSerializer (many = True)},
)       
class CustomeCreateView(CreateAPIView):
    
    queryset = Customer.objects.all()
    
    serializer_class = CustomerSerializer
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
'''PRODUCT VIEW''' 
               
# Product View    

@extend_schema(
  tags = ['Product'],
  
  responses = {200: ProductSerializer (many = True)},
)

class ProductListView(ListAPIView):
    
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
    


@extend_schema(
  tags = ['Product'],
  
  responses = {201: ProductSerializer (many = True)},
)  
class ProductCreateView(CreateAPIView):
    
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
# Handle exception
    
    def post(self, request,*args,**kwargs):
        try:
            return super().post(request,*args,**kwargs)
        except IntegrityError:
            raise APIEXCEPTION ('Database integrity error')
        except Exception as e:
            raise APIEXCEPTION ('Error Creating product')
# I added it to validate price

    def validate_price(self, value):
         if not value:
             raise serializers.ValidationError('price is required')


'''SALE VIEW'''    
            
# Sale Views    
@extend_schema(
  tags = ['Sale'],
  
  responses = {200: SaleSerializer (many = True)},
)       
class SaleListView(ListAPIView):
    queryset = Sale.objects.all()
    
    serializer_class = SaleSerializer
    
    permission_classes = [IsAuthenticated]
    

@extend_schema(
  tags = ['Sale'],
  
  responses = {201:SaleSerializer (many = True)},
)    
class SaleCreateView(CreateAPIView):
    
    queryset = Sale.objects.all()
    
    serializer_class = ProductSerializer
    
    permission_classes = [IsAuthenticated]
    
 
'''MARKET VIEW'''

#Market Views      
@extend_schema(
  tags = ['Market_Trend'],
  
  responses = {200: ProductSerializer (many = True)},
)       
class Market_TrendListView(ListAPIView):
    
    queryset = Market_Trend.objects.all()
    
    serializer_class = Market_TrendSerializer
    
    permission_classes = [IsAuthenticated]
    
    
@extend_schema(
  tags = ['Market_Trend'],
  
  responses = {201: Market_TrendSerializer (many = True)},
)
class Market_TrendCreateView(CreateAPIView):
    
    queryset = Market_Trend.objects.all()
    
    serializer_class = Market_TrendSerializer
    
    permission_classes = [IsAuthenticated]
    