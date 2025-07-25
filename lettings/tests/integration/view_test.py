import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestViewsIntegration:
    """Integration tests for view routing and data rendering."""

    def test_index_to_detail_navigation(self, test_client, multiple_lettings):
        index_response = test_client.get(reverse('lettings:index'))
        assert index_response.status_code == 200

        for letting in multiple_lettings:
            detail_url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
            assert detail_url.encode() in index_response.content

            detail_response = test_client.get(detail_url)
            assert detail_response.status_code == 200
            assert detail_response.context['title'] == letting.title
            assert detail_response.context['address'] == letting.address
