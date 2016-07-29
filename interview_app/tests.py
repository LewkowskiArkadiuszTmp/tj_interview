from django.test import TestCase
from django.core.urlresolvers import reverse
import json


class IndexViewTests(TestCase):

    def test_index_view_return_empty_json(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {})

    def test_index_view_return_valid_json_format(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
                             "html": "", "title": "", "description": ""})

    def test_index_view_passing_url_parameter(self):
        response = self.client.get(
            reverse('index', kwargs={"url_parameter": "http://wi.pb.bialystok.pl"}))
        self.assertEqual(response.status_code, 200)

    def test_index_view_return_title(self):
        response = self.client.get(
            reverse('index', kwargs={"url_parameter": "http://wi.pb.bialystok.pl"}))
        self.assertEqual(response.status_code, 200)
        content_as_json = json.loads(response.content)
        self.assertEqual(content_as_json['title'], "Aragorn Server")

    def test_index_view_return_description(self):
        response = self.client.get(
            reverse('index', kwargs={"url_parameter": "http://wi.pb.bialystok.pl"}))
        content_as_json = json.loads(response.content)
        self.assertEqual(content_as_json[
                     'description'], "Instytut Informatyki, Dydaktyka, Sieci, Podstawy Informatyki")
