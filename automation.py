import unittest
from flask_init import app
class Tester(unittest.TestCase):
	def test_init_server(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)
		
	def test_Failure(self):
		tester = app.test_client(self)
		response = tester.get('a', content_type='html/text')
		self.assertEqual(response.status_code, 404)
		

if __name__ == '__main__':
	unittest.main()

