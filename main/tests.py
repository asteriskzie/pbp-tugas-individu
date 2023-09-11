from django.test import TestCase, Client
from main.models import Jam

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class cobaTest(TestCase): 
    def setUp(self): 
        pass
    
    