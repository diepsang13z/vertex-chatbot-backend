import unittest

from fastapi.testclient import TestClient

from main import app

SEND_MESSAGE_TO_GEMINI_URL = '/gemini/chat'


class TestGemini(unittest.TestCase):
    """Test gemini API requests."""

    def setUp(self):
        self.client = TestClient(app)

    def test_send_message(self):
        payload = {'message': 'Who are you?'}
        response = self.client.post(SEND_MESSAGE_TO_GEMINI_URL, json=payload)

        # Test status code success
        assert response.status_code == 200
        response_body = response.json()

        # Test assistant tunning
        assert response_body["assistant"] is not None
        assert response_body["assistant"] != ""
        assert 'GDG' in response_body['assistant']


if __name__ == "__main__":
    unittest.main()
