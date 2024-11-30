import unittest
from unittest.mock import patch, MagicMock

from app.database import get_db


class TestDB(unittest.TestCase):

    @patch('app.database.Session')
    def test_get_db(self, MockSession):
        """Test database connection."""
        # Create a mock session object
        mock_session = MagicMock()
        MockSession.return_value = mock_session

        # Call the generator function to fetch the session
        db_generator = get_db()
        db = next(db_generator)

        # Check that the Session() was called once
        MockSession.assert_called_once()

        # Check if the returned object is the mocked session
        self.assertEqual(db, mock_session)

        # Ensure the session is properly closed after use
        db_generator.close()
        mock_session.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
