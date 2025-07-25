import pytest
from django.urls import resolve, reverse


@pytest.mark.django_db
class TestUrlsIntegration:
    """Integration tests for URL routing with actual requests."""

    def test_index_url_returns_all_lettings(self, test_client, multiple_lettings):
        response = test_client.get('/lettings/')
        assert response.status_code == 200
        for letting in multiple_lettings:
            assert letting.title.encode() in response.content

    def test_detail_urls_for_all_lettings(self, test_client, multiple_lettings):
        for letting in multiple_lettings:
            response = test_client.get(f'/lettings/{letting.id}/')
            assert response.status_code == 200
            assert letting.title.encode() in response.content
            assert str(letting.address.number).encode() in response.content

    def test_nonexistent_letting_url(self, test_client, multiple_lettings):
        invalid_id = max(l.id for l in multiple_lettings) + 100
        response = test_client.get(f'/lettings/{invalid_id}/')
        assert response.status_code == 404

    def test_url_reverse_and_resolve_consistency(self, test_client, multiple_lettings):
        for letting in multiple_lettings:
            url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
            resolved = resolve(url)
            assert resolved.view_name == 'lettings:letting'
            assert resolved.kwargs['letting_id'] == letting.id

            response = test_client.get(url)
            assert response.status_code == 200
