from django.test import TestCase
from django.test.client import Client
import unittest


class CallTest(TestCase):

    def test_http(self):
        response = self.client.get('/call/')
        self.failUnlessEqual(response.status_code, 200)
