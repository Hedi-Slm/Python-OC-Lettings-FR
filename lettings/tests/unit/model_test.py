import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    """Unit tests for the Address model."""

    def test_address_creation_valid_data(self, sample_address):
        """Test creating an address with valid data."""
        assert sample_address.number == 123
        assert sample_address.street == "Main Street"
        assert sample_address.city == "New York"
        assert sample_address.state == "NY"
        assert sample_address.zip_code == 10001
        assert sample_address.country_iso_code == "USA"

    def test_address_str_method(self, sample_address):
        """Test the string representation of an address."""
        assert str(sample_address) == "123 Main Street"

    def test_address_verbose_name(self):
        """Test the verbose name configuration."""
        assert Address._meta.verbose_name == "Address"
        assert Address._meta.verbose_name_plural == "Addresses"

    def test_address_field_validators(self, invalid_address, long_street, long_city):
        """Test all validation constraints on address fields."""
        with pytest.raises(ValidationError):
            invalid_address.full_clean()

        with pytest.raises(ValidationError):
            Address(
                number=123,
                street=long_street,
                city="Valid City",
                state="TX",
                zip_code=12345,
                country_iso_code="USA"
            ).full_clean()

        with pytest.raises(ValidationError):
            Address(
                number=123,
                street="Test Street",
                city=long_city,
                state="TX",
                zip_code=12345,
                country_iso_code="USA"
            ).full_clean()


@pytest.mark.django_db
class TestLettingModel:
    """Unit tests for the Letting model."""

    def test_letting_creation_valid_data(self, another_address):
        """Test creating a letting with valid data."""
        letting = Letting.objects.create(
            title="Modern Loft",
            address=another_address
        )
        assert letting.title == "Modern Loft"
        assert letting.address == another_address

    def test_letting_str_method(self, letting_with_custom_address):
        """Test the string representation of a letting."""
        assert str(letting_with_custom_address) == "Cozy Studio"

    def test_letting_one_to_one_relationship(self, another_address):
        """Test the OneToOne relationship between Letting and Address."""
        letting = Letting.objects.create(
            title="Modern Loft",
            address=another_address
        )
        assert letting.address == another_address
        assert another_address.new_letting == letting

    def test_letting_title_max_length(self, long_title, another_address):
        """Test that title field respects maximum length constraint."""
        with pytest.raises(ValidationError):
            letting = Letting(
                title=long_title,
                address=another_address
            )
            letting.full_clean()

    def test_letting_unique_address_constraint(self, another_address):
        """Test that each address can only have one letting (OneToOneField)."""
        Letting.objects.create(
            title="First Letting",
            address=another_address
        )

        with pytest.raises(IntegrityError):
            Letting.objects.create(
                title="Second Letting",
                address=another_address
            )
