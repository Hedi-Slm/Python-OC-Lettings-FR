import pytest


@pytest.mark.django_db
class TestProfileModel:
    def test_profile_str_method(self, profile_john):
        assert str(profile_john) == "john_doe"

    def test_favorite_city_field(self, profile_jane):
        assert profile_jane.favorite_city == "Paris"

    def test_profile_user_relation(self, profile_john):
        assert profile_john.user.username == "john_doe"
        assert profile_john.user.new_profile == profile_john
