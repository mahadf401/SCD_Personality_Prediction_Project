import unittest
from app import app

class FlaskTest(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True

    # Test home page
    def test_home_page(self):

        response = self.app.get('/')

        self.assertEqual(
            response.status_code,
            200
        )

    # Test API route
    def test_api(self):

        response = self.app.get('/api/test')

        self.assertEqual(
            response.status_code,
            200
        )

if __name__ == "__main__":
    unittest.main()