from django.db import models

from account.models import User
class BaseModel(models.Model):
    id = models.UUIDField(unique = True, default = uuid.uuid4, editable = False, primary_key = True) 
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        
        abstract = True

class Payment(BaseModel):
    
    user = models.ForeignKey(User,on_delete = models.CASCADE)    

    bank_used = models.CharField(max_length=100)
    
    bank_account_name = models.CharField(max_length=100)
    
    date_of_transaction = models.DateField()
    receipt = models.ImageField(upload_to='receipts/')
    
    payment_status = models.CharFields(max_length = 100, default = 'pending')
    
    amount = models.DecimalField(max_length = 10, decimal_places = 2)   
    
    def __str__(self):
        return f'{self.bank_account_name} - {self.bank_used}'