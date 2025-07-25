import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestHomeIndexView:

    @pytest.fixture(autouse=True)
    def setup(self, test_client):
        self.client = test_client
        self.url = reverse('index')

    def test_homepage_response_status(self):
        response = self.client.get(self.url)
        assert response.status_code == 200

    def test_homepage_template_used(self):
        response = self.client.get(self.url)
        assert 'index.html' in [t.name for t in response.templates]

    def test_homepage_content(self):
        response = self.client.get(self.url)
        # Add content expectations based on your actual template
        assert b"Welcome" in response.content or b"Lettings" in response.content
