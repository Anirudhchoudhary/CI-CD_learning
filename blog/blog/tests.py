from django.test import TestCase
from django.urls import reverse


class MyViewTest(TestCase):
    def test_index_view(self):
        """Test that the index view returns a 200 status code."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
