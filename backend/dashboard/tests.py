import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Dashboard,Widget

from .serializers import DashboardSerializer

from rest_framework import status 
# Create your tests here.


@pytest.fixure
def widget_data():
    return {'type':'widget'}
    

@pytest.fixture
def dashboard_data():
    return {'name':'New order'}
 
# Dashboard Test   
def test_dashboard_list_view(api_client):
    url = reverse ('dashboard-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_dashboard_create_view(api_client, dashboard_data):
    url = reverse ('dashboard-list')
    response = api_client.post(url, dashboard_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED


# Widget Test

def test_widget_list_view(api_client):
    url = reverse ('widget-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_widget_create_view(api_client,widget_data):
    url = reverse ('widget-list')
    response = api_client.post(url,widget_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED
