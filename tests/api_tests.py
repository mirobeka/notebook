from notebook import create_app
import unittest

class NotebookAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_discovery_string(self):
        uri = '/api/v1/'
        rv = self.client.get(uri, follow_redirects=True)
        expected = "You've discovered notebook api!"
        self.assertEqual(rv.data, expected)
