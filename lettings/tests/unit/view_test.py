import pytest
from django.urls import reverse
from lettings.views import index, letting


@pytest.mark.django_db
class TestIndexView:
    """Tests for the index view."""

    @pytest.fixture(autouse=True)
    def setup(self, test_client):
        self.client = test_client
        self.url = reverse('lettings:index')

    def test_index_view_empty_lettings(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert 'lettings_list' in response.context
        assert list(response.context['lettings_list']) == []
        assert b'No lettings are available.' in response.content

    def test_index_view_with_lettings(self, multiple_lettings):
        response = self.client.get(self.url)
        lettings_list = list(response.context['lettings_list'])

        assert response.status_code == 200
        assert 'lettings_list' in response.context
        assert len(lettings_list) == len(multiple_lettings)

        for letting in multiple_lettings:
            assert letting in lettings_list
            assert letting.title.encode() in response.content

        assert b'No lettings are available.' not in response.content



@pytest.mark.django_db
class TestLettingDetailView:
    """Tests for the letting detail view."""

    @pytest.fixture(autouse=True)
    def setup(self, test_client, test_letting):
        self.client = test_client
        self.letting = test_letting
        self.url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})

    def test_letting_detail_view_valid_id(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert response.context['title'] == self.letting.title
        assert response.context['address'] == self.letting.address

    def test_letting_detail_view_invalid_id(self):
        invalid_url = reverse('lettings:letting', kwargs={'letting_id': 99999})
        response = self.client.get(invalid_url)
        assert response.status_code == 404

    def test_letting_detail_view_context_data(self):
        response = self.client.get(self.url)
        assert response.context['title'] == self.letting.title
        assert response.context['address'] == self.letting.address

    def test_view_functions_directly(self, request_factory, multiple_lettings):
        request = request_factory.get('/lettings/')
        response = index(request)
        assert response.status_code == 200

        letting_obj = multiple_lettings[0]
        request = request_factory.get(f'/lettings/{letting_obj.id}/')
        response = letting(request, letting_obj.id)
        assert response.status_code == 200
