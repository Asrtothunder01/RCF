from  django.contrib import admin
from .models import Payment

@admin.register(Payment)

class PaymentAdmin(admin.ModelAdmin):
    
    list_display = ('bank_used','date_of_transaction','amount')
    
    search_fields = ('bank_used','date_of_transaction','amount')
    
    date_hierarchy = 'date_of_transaction'
    
    list_filter = ('bank_used',)
    
  