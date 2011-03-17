from django.test import TestCase
from mysite.contact.models import Person


class ContactTest(TestCase):
    fixtures=['initial_data.json']

    def test_http(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        contact=Person.objects.get(last_name="Ganziy")
        self.assertContains(response, contact.first_name,
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, contact.last_name,
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, 'Sept. 24, 1986',
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, contact.bio,
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, contact.mail,
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, contact.jabber,
                            count=2, status_code=200, msg_prefix='')
        self.assertContains(response, contact.skype,
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, contact.other,
                            count=1, status_code=200, msg_prefix='')
        self.assertTemplateUsed(response, 'base.html', msg_prefix='')
