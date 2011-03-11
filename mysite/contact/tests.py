from django.test.client import Client
from django.test import TestCase
from mysite.contact.models import Persone
import unittest

class ContactTest(TestCase):
    fixtures=['initial_data.json']

    def setUp(self):
       contact=Persone.objects.all()
       self.count=contact.count()
       contact2=Persone.objects.filter(last_name="Ganziy")
       self.assertEqual(self.count, contact2.count())
 
    def test_base(self):
        self.contact=Persone.objects.create(first_name="Ivanov", last_name="Ivan", mail="ivanov@gmail", date="1945-01-01")
        contact_count2=Persone.objects.all()
        self.assertNotEqual(self.count, contact_count2.count())
        self.contact.delete()
        contact_count2=Persone.objects.all()
        self.assertEqual(self.count, contact_count2.count())
 
