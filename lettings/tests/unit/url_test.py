import pytest
from django.urls import reverse, resolve
from lettings import views


@pytest.mark.django_db
class TestLettingsUrls:
    """Unit tests for the lettings app URL configuration."""

    def test_lettings_index_url_reverse(self):
        url = reverse('lettings:index')
        assert url == '/lettings/'

    def test_lettings_index_url_resolve(self):
        resolver = resolve('/lettings/')
        assert resolver.view_name == 'lettings:index'
        assert resolver.func == views.index

    def test_lettings_detail_url_reverse(self, test_letting):
        url = reverse('lettings:letting', kwargs={'letting_id': test_letting.id})
        assert url == f'/lettings/{test_letting.id}/'

    def test_lettings_detail_url_resolve(self, test_letting):
        resolver = resolve(f'/lettings/{test_letting.id}/')
        assert resolver.view_name == 'lettings:letting'
        assert resolver.func == views.letting
        assert resolver.kwargs == {'letting_id': test_letting.id}

    def test_lettings_index_url_accessibility(self, test_client):
        response = test_client.get('/lettings/')
        assert response.status_code == 200

    def test_lettings_detail_url_accessibility(self, test_client, test_letting):
        response = test_client.get(f'/lettings/{test_letting.id}/')
        assert response.status_code == 200

    def test_lettings_detail_url_with_different_ids(self):
        for test_id in [1, 999, 12345]:
            url = reverse('lettings:letting', kwargs={'letting_id': test_id})
            assert url == f'/lettings/{test_id}/'
            resolver = resolve(f'/lettings/{test_id}/')
            assert resolver.view_name == 'lettings:letting'
            assert resolver.kwargs == {'letting_id': test_id}
