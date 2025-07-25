import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestProfileIndexView:
    @pytest.fixture(autouse=True)
    def setup(self, test_client):
        self.client = test_client
        self.url = reverse("profiles:index")

    def test_index_view_no_profiles(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert "profiles_list" in response.context
        assert list(response.context["profiles_list"]) == []

    def test_index_view_with_profiles(self, multiple_profiles):
        response = self.client.get(self.url)
        assert response.status_code == 200
        for prof in multiple_profiles:
            assert prof in response.context["profiles_list"]
            assert prof.user.username.encode() in response.content


@pytest.mark.django_db
class TestProfileDetailView:
    @pytest.fixture(autouse=True)
    def setup(self, test_client, profile_john):
        self.client = test_client
        self.username = profile_john.user.username
        self.url = reverse("profiles:profile", kwargs={"username": self.username})
        self.profile = profile_john

    def test_profile_detail_valid_user(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert response.context["profile"] == self.profile
        assert self.profile.favorite_city.encode() in response.content
        assert self.profile.user.username.encode() in response.content

    def test_profile_detail_invalid_user(self):
        invalid_url = reverse("profiles:profile", kwargs={"username": "fake_user"})
        response = self.client.get(invalid_url)
        assert response.status_code == 404
