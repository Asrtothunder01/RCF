from django.urls import path
from .views import PaymentCreate, PaymentList

urlpatterns = [
    path('v1/', PaymentList.as_view(),name = 'payment_list'),
    path('v2/', PaymentCreate.as_view(),name = 'payment_create'),

]