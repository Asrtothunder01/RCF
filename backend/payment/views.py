from rest_framework.generics import CreateAPIView,ListAPIView

from rest_framework.permissions import IsAuthenticated
from .models import Payment

from rest_framework import permissions

from .serializers import PaymentSerializer

from drf_spectacular.utils import extend_schema


""" Payment View"""

@extend_schema(
 tags = ['Payment'],
 responses = {200:PaymentSerializer (many = True)},
)


# PAYMENTLISTVIEW
class PaymentList(APIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer
	permission_classes = [permissions.IsAuthenticated]
    pagination_class = None



# PAYMENTCREATE VIEW
@extend_schema(
  tags = ['Payment'],
  responses = {201: PaymentSerializer(many = True)},
)	

class PaymentCreate(CreateAPIView):
	queryset = Payment.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PaymentSerializer
	pagination_class = None