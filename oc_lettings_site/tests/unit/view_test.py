import pytest
from oc_lettings_site.views import index


@pytest.mark.django_db
class TestIndexFunction:
    def test_direct_view_call(self, request_factory):
        request = request_factory.get('/')
        response = index(request)
        assert response.status_code == 200
