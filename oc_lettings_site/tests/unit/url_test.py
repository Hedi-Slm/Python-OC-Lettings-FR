import pytest
from django.urls import reverse, resolve
from oc_lettings_site import views


@pytest.mark.django_db
class TestMainUrls:

    def test_root_url_reverse(self):
        url = reverse('index')
        assert url == '/'

    def test_root_url_resolves(self):
        resolver = resolve('/')
        assert resolver.func == views.index
        assert resolver.view_name == 'index'

    def test_included_lettings_urls(self):
        url = reverse('lettings:index')
        assert url.startswith('/lettings/')

    def test_included_profiles_urls(self):
        url = reverse('profiles:index')
        assert url.startswith('/profiles/')
