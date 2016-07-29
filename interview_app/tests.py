from django.test import TestCase
from django.core.urlresolvers import reverse
import json
import hashlib


class IndexViewTests(TestCase):

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

    def test_index_view_return_html(self):
        response = self.client.get(
            reverse('index', kwargs={"url_parameter": "http://wi.pb.bialystok.pl"}))
        content_as_json = json.loads(response.content)
        # jedyny sposob jaki znalazlem na poprawne porownanie duzych stringow
        html_hash_good = '76bc09f46e153991289c278279f03f99'
        html_hash_test = hashlib.md5(
            content_as_json['html'].encode('utf-8')).hexdigest()
        self.assertEqual(html_hash_good, html_hash_test)

    def test_wrong_url_name(self):
        response = self.client.get(
            reverse('index', kwargs={"url_parameter": "www.wi.pb.bialystok.pl"}))
        self.assertEqual(response.status_code, 404)
