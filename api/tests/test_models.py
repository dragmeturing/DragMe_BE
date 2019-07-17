from django.test import TestCase
from api.models import Shows, Lineup


class ShowTest(TestCase):
       def test_home_page_status_code(self):
           response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        def setUp(self):
            pass  

        def tearDown(self): 
            pass
        
        def failed(self):
            print 'Fail'