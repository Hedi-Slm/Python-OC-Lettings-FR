import pytest
from django.urls import reverse
from profiles.views import index, profile


@pytest.mark.django_db
class TestViewFunctions:
    def test_index_function_directly(self, request_factory, multiple_profiles):
        request = request_factory.get("/profiles/")
        response = index(request)
        assert response.status_code == 200
        for profile in multiple_profiles:
            assert profile.user.username.encode() in response.content

    def test_profile_function_directly(self, request_factory, profile_jane):
        request = request_factory.get(f"/profiles/{profile_jane.user.username}/")
        response = profile(request, username=profile_jane.user.username)
        assert response.status_code == 200
        assert profile_jane.favorite_city.encode() in response.content
