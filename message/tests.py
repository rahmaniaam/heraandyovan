from django.test import TestCase

# Create your tests here.
class Dudu(TestCase):
	def test_index_url_is_exist(self):
        response = Client().get('/message/')
        self.assertEqual(response.status_code, 200)