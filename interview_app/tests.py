from django.test import TestCase
from django.core.urlresolvers import reverse

class IndexViewTests(TestCase):

    # test czy zwraca json
    def index_view_return_empty_json(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {})
