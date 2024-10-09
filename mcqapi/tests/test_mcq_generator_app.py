import unittest
import json
from app import create_app


class MCQApiTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.app = create_app()
        self.client= self.app.test_client()
        self.app.testing = True
        

    def test_fetch_questions(self):
        """Test fetching questions for a specific skill."""
        response = self.client.get('/test?skill=finance')
        print(response)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertIn('quests', data)
        self.assertEqual(len(data['quests']), 5)  # Adjust based on your expected number of questions
        

    def test_invalid_skill(self):
        """Test fetching questions for a non-existing skill."""
        response = self.client.get('/test?skill=Pythonish')
        self.assertEqual(response.status_code, 404)  

if __name__ == '__main__':
    unittest.main()

