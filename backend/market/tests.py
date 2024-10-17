import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Customer, Sale, Product, Market_trend

from .serializers import CustomerSerializer, SaleSerializer, ProductSerializer, Market_TrendSerializer

from rest_framework import status 
# Create your tests here.


@pytest.fixture
def sale_data():
    return {'sale_amount':'100'}
    
@pytest.fixture
def product_data():
    return {'name':'paste'}
    
@pytest.fixture
def market_trend():
    return {'trend_name':'iphone'}

@pytest.fixture
def customer_data():
    return {'first_name':'daniel'}
    
    
def test_customer_list_view(api_client):
    url = reverse ('customer-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_customer_create_view(api_client,customer_data):
    url = reverse ('customer-list')
    response = api_client.post(url,customer_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED




def test_product_list_view(api_client):
    url = reverse ('product-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_product_create_view(api_client,product_data):
    url = reverse ('product-list')
    response = api_client.post(url,product_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED
    
    
    
    
def test_sale_list_view(api_client):
    url = reverse ('sale-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_sale_create_view(api_client,sale_data):
    url = reverse ('sale-list')
    response = api_client.post(url,sale_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED
    
    
def test_market_trend_list_view(api_client):
    url = reverse ('market_trend-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_market_trend_create_view(api_client, market_trend_data):
    url = reverse ('market_trend-list')
    response = api_client.post(url,market_trend_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED
