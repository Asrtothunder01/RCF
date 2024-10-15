from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('v1/',views.CustomerListView.as_view(),name = 'Customer_list'),
  
  path('v2/',views.CustomerCreateView.as_view(), name = 'Customer_create'),
  
  path('product/v1/',views.ProductListView.as_view(),name = 'product_list'),
  
  path('product/v2/',views.ProductCreateView.as_view(), name = 'product_create'),
  
  path('sale/v1/',views.SaleListView.as_view(),name = 'sale_list'),
  
  path('sale/v2/',views.SaleCreateView.as_view(), name = 'sale_create'),
   
  path('trend/v1/', views.Market_TrendListView.as_view(),name = 'Trend_list'),
  
  path('trend/v2/', views.Market_TrendCreateView.as_view(),name = 'Trend_create')
  

]