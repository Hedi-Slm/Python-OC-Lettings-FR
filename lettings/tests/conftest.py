"""
Pytest configuration and fixtures for the lettings app tests.
"""

import pytest
from django.test import Client, RequestFactory
from lettings.models import Address, Letting


# --- Common Utilities ---

@pytest.fixture
def test_client():
    """Provide a Django test client."""
    return Client()


@pytest.fixture
def request_factory():
    """Provide a Django RequestFactory instance."""
    return RequestFactory()


# --- Address Fixtures ---

@pytest.fixture
def sample_address():
    """A basic reusable address."""
    return Address.objects.create(
        number=123,
        street="Main Street",
        city="New York",
        state="NY",
        zip_code=10001,
        country_iso_code="USA"
    )


@pytest.fixture
def another_address():
    """Another valid address."""
    return Address.objects.create(
        number=555,
        street="Broadway",
        city="Seattle",
        state="WA",
        zip_code=98101,
        country_iso_code="USA"
    )


@pytest.fixture
def invalid_address():
    """Return an unsaved invalid Address instance."""
    return Address(
        number=10000,  # Invalid: too high
        street="A" * 65,  # Invalid: too long
        city="Test City",
        state="T",  # Invalid: too short
        zip_code=100000,  # Invalid: too high
        country_iso_code="US"  # Invalid: too short
    )


# --- Letting Fixtures ---

@pytest.fixture
def sample_letting(sample_address):
    """Create a letting linked to the sample address."""
    return Letting.objects.create(
        title="Sample Letting",
        address=sample_address
    )


@pytest.fixture
def test_letting():
    """Letting used for view and URL tests."""
    address = Address.objects.create(
        number=555,
        street="Broadway",
        city="Seattle",
        state="WA",
        zip_code=98101,
        country_iso_code="USA"
    )
    return Letting.objects.create(title="Downtown Apartment", address=address)


@pytest.fixture
def letting_with_custom_address():
    """Letting with different address for string representation test."""
    address = Address.objects.create(
        number=321,
        street="Elm Street",
        city="Miami",
        state="FL",
        zip_code=33101,
        country_iso_code="USA"
    )
    return Letting.objects.create(
        title="Cozy Studio",
        address=address
    )


@pytest.fixture
def multiple_lettings():
    """Multiple lettings for integration or index view tests."""
    lettings = []
    for i in range(3):
        address = Address.objects.create(
            number=100 + i,
            street=f"Test Street {i}",
            city=f"Test City {i}",
            state="TX",
            zip_code=10000 + i,
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title=f"Test Letting {i}",
            address=address
        )
        lettings.append(letting)
    return lettings


# --- Validation Edge Case Fixtures ---

@pytest.fixture
def long_title():
    """Invalid long letting title."""
    return "A" * 257  # max_length=256


@pytest.fixture
def long_street():
    """Invalid long street name."""
    return "A" * 65  # max_length=64


@pytest.fixture
def long_city():
    """Invalid long city name."""
    return "B" * 65  # max_length=64
