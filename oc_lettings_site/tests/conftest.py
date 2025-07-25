import pytest
from django.test import Client, RequestFactory


@pytest.fixture
def test_client():
    """Provide a Django test client."""
    return Client()


@pytest.fixture
def request_factory():
    """Provide a Django RequestFactory instance."""
    return RequestFactory()
