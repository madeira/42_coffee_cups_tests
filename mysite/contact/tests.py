from django.test import TestCase
from mysite.contact.models import Person


class ContactTest(TestCase):
    fixtures=['initial_data.json']

    def test_http(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        contact = Person.objects.get(last_name="Ganziy")
        self.assertContains(response, contact.first_name)
        self.assertContains(response, contact.last_name)
        self.assertContains(response, 'Sept. 24, 1986')
        self.assertContains(response, contact.bio)
        self.assertContains(response, contact.mail)
        self.assertContains(response, contact.jabber)
        self.assertContains(response, contact.skype)
        self.assertContains(response, contact.other)
        self.assertTemplateUsed(response, 'base.html')

    def test_error_multipleobjectsreturned(self):
        self.contact = Person.objects.create(last_name="Ganziy", date="1986-09-24")
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'returned more than one Person')
        self.assertTemplateUsed(response, 'base.html')
        self.contact.delete()

    def test_error_doesnotexist(self):
        Person.objects.all().delete()
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Person matching query does not exist')
        self.assertTemplateUsed(response, 'base.html')
