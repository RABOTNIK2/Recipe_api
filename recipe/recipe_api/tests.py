from django.test import TestCase
from urllib.parse import urlencode
from .models import *
from django.urls import reverse

class TestCategory(TestCase):
    def test_list(self):
        response = self.client.get('/recipe_api/catlist/')
        self.assertEqual(response.status_code, 200)
    
    def test_create(self):
        data = urlencode({'name': 'gnida'})
        response = self.client.post('/recipe_api/cat_create/', data, content_type="application/x-www-form-urlencoded")
        self.assertEqual(response.status_code, 201)
        
    def setUp(self):
        self.category = Category.objects.create(name = 'Огрызки')
        
    
            
    

# Create your tests here.
