from django.test import TestCase
from django.test import SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse
from django.db import models


from .models import Shows


class Show(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

