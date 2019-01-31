from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please Log in' in response.data)

    def test_correct_load(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'You are logged in', response.data)    
        
    def test_incorrect_load(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="wrong", password="wrong"), follow_redirects=True)
        self.assertIn(b'Invalid credentials. Please try again', response.data) 

    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You are logged out', response.data)

    def test_login_required(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to log in first' in response.data)

    def test_table_post(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'I love guitars', response.data)   

if __name__ == "__main__":
    unittest.main() 