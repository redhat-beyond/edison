
import unittest
import requests

from flask_init import index



class Tester(unittest.TestCase):
    def test_request_response(self):
    	response = requests.get("http://127.0.0.1:5000")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
