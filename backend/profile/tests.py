import pytest

from django.urls import reverse

from rest_framework.test import APIClient

from .models import Profile

from .serializers import ProfileSerializer

from rest_framework import status

# Profile Test

def test_profile_list_view(api_client):
    url = reverse ('profile-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

def test_profile_create_view(api_client, profile_data):
    url = reverse ('profile-list')
    response = api_client.post(url, profile_data, format = 'json')
    assert response.status_code == status.HTTP_201_CREATED