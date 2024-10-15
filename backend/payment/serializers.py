from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','bank_used', 'bank_account_name', 'date_of_transaction', 'receipt','created_at']
        read_only_fields = ['id','bank_account_name','date_of_transaction']