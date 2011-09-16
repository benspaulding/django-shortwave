from django.core.urlresolvers import reverse
from django.test import TestCase

from shortwave.models import CommandTriggerField


class ShortwaveTestCase(TestCase):
    """"""

    fixtures = ['shortwave-test-data']
    urls = 'shortwave.tests.urls'


class ModelsTestCase(ShortwaveTestCase):
    """"""

    def test_command_trigger_field(self):
        pass


class FormsTestCase(ShortwaveTestCase):
    """"""

    def test_command_trigger_field(self):
        pass


class ViewsTestCase(ShortwaveTestCase):
    """Test Views, URLs, and templates."""

    def test_list(self):
        # Be sure we don't mess with named urls.
        request_url = reverse('shortwave_wave_list')
        response = self.client.get(request_url)
        self.assertEqual(response.request['PATH_INFO'], '/shortwave/')
        self.assertEqual(response.status_code, 200)
        self.failUnless(response['Content-Type'], 'text/html; charset=utf-8')
        self.assertTemplateUsed(response, 'shortwave/wave_list.html')
        self.failUnless(response.context['wave_list'])
        self.assertContains(response, 'foobar')
        self.assertContains(response, 'bazboo')
        self.assertNotContains(response, 'wowee')

    def test_detail_1(self):
        request_url = reverse('shortwave_wave_detail', kwargs={'username': 'foobar'})
        response = self.client.get(request_url)
        self.assertEqual(response.request['PATH_INFO'], '/shortwave/foobar/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain; charset=utf-8')
        self.assertTemplateUsed(response, 'shortwave/wave_detail.txt')
        self.failUnless(response.context['wave'])
        # Test that the kill-defaults flag is not only present, but
        # also the very first text.
        self.failUnless(response.content.lstrip().startswith('> #kill-defaults'))

    def test_detail_2(self):
        request_url = reverse('shortwave_wave_detail', kwargs={'username': 'bazboo'})
        response = self.client.get(request_url)
        self.assertEqual(response.request['PATH_INFO'], '/shortwave/bazboo/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/plain; charset=utf-8')
        self.assertTemplateUsed(response, 'shortwave/wave_detail.txt')
        self.failUnless(response.context['wave'])
        self.assertNotContains(response, '> #kill-defaults')
        # Test wave syntax and that neither url nor description are escaped.
        self.assertContains(response, 'map http://www.google.com/maps?q=%s&foo=bar Google Maps <search>')

    def test_detail_3(self):
        request_url = reverse('shortwave_wave_detail', kwargs={'username': 'wowee'})
        response = self.client.get(request_url)
        self.assertEqual(response.request['PATH_INFO'], '/shortwave/wowee/')
        # This is user is not active, so we should get a 404.
        self.assertEqual(response.status_code, 404)
