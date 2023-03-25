from django.test import TestCase

# Create your tests here.


class ViewsTestCase(TestCase):
    def test_banks_list_api(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/banking/banks/')
        self.assertEqual(response.status_code, 200)

    def test_banks_detail_api(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/banking/banks/1/')
        self.assertEqual(response.status_code, 404)

    def test_branches_list_api(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/banking/branches/')
        self.assertEqual(response.status_code, 200)




