import pytest
from django.contrib.auth.models import User
from django.test import Client, RequestFactory
from profiles.models import Profile


# --- Common Utilities ---

@pytest.fixture
def test_client():
    return Client()


@pytest.fixture
def request_factory():
    return RequestFactory()


# --- User & Profile Fixtures ---

@pytest.fixture
def user_john():
    return User.objects.create_user(username="john_doe", password="secret")


@pytest.fixture
def user_jane():
    return User.objects.create_user(username="jane_doe", password="pass123")


@pytest.fixture
def profile_john(user_john):
    return Profile.objects.create(user=user_john, favorite_city="New York")


@pytest.fixture
def profile_jane(user_jane):
    return Profile.objects.create(user=user_jane, favorite_city="Paris")


@pytest.fixture
def multiple_profiles(user_john, user_jane):
    profile1 = Profile.objects.create(user=user_john, favorite_city="New York")
    profile2 = Profile.objects.create(user=user_jane, favorite_city="Paris")
    return [profile1, profile2]
