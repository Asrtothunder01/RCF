from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Payment
        fields = ['id','user','bank_used', 'bank_account_name', 'date_of_transaction','amount','payment_status','receipt','created_at']
        read_only_fields = ['id','bank_account_name','date_of_transaction','amount']