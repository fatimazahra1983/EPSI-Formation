import unittest

from fastapi.testclient import TestClient
from main import app


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.api_client = TestClient(app=app)

    def test_get_ok(self):
        response = self.api_client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"message": "Hello world!"}, response.json())
