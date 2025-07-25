import pytest
from django.urls import reverse, resolve
from profiles import views


@pytest.mark.django_db
class TestProfilesUrls:
    def test_index_url_reverse(self):
        assert reverse("profiles:index") == "/profiles/"

    def test_profile_url_reverse(self, profile_john):
        assert reverse("profiles:profile", kwargs={"username": "john_doe"}) == "/profiles/john_doe/"

    def test_index_url_resolves_to_view(self):
        resolver = resolve("/profiles/")
        assert resolver.func == views.index
        assert resolver.view_name == "profiles:index"

    def test_profile_url_resolves_to_view(self, profile_john):
        resolver = resolve("/profiles/john_doe/")
        assert resolver.func == views.profile
        assert resolver.view_name == "profiles:profile"
        assert resolver.kwargs == {"username": "john_doe"}
