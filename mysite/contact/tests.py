from django.test import TestCase
from mysite.contact.models import Person
from django.conf import settings


class ContactTest(TestCase):
    fixtures = ['initial_data.json']

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

    def test_processor(self):
        response = self.client.get('/processor/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, settings.TIME_ZONE)
        self.assertContains(response, settings.LANGUAGE_CODE)
        self.assertContains(response, settings.PROJECT_PATH)

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

    def test_login(self):
        response = self.client.get('/accounts/login/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.login(username='username', password='password')
        self.assertEqual(response, False)
        response = self.client.get('/edit/')
        self.failUnlessEqual(response.status_code, 302)
        response = self.client.login(username='admin', password='admin')
        self.assertEqual(response, True)
        response = self.client.get('/edit/')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.post('/edit/', {'first_name': '', 'last_name': 'Ganziy',
                                               'date': '1986-09', 'bio': 'Dmitry',
                                               'mail': 'Dmitry', 'jabber': 'Dmitry',
                                               'skype': 'Dmitry', 'other': 'Dmitry'},
                                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertContains(response, 'This field is required')
        self.assertContains(response, 'Enter a valid date')
        self.assertContains(response, 'Enter a valid e-mail address')
        self.failUnlessEqual(response.status_code, 200)
        response = self.client.post('/edit/', {'first_name': 'Dmitry', 'last_name': 'Ganziy',
                                               'date': '1986-09-24', 'bio': 'Dmitry',
                                               'mail': 'Dmitry@dmitry.ua', 'jabber': 'Dmitry',
                                               'skype': 'Dmitry', 'other': 'Dmitry'},
                                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Dmitry')
        response = self.client.get('/edit/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Dmitry')
        self.client.logout()
        response = self.client.get('/edit/')
        self.failUnlessEqual(response.status_code, 302)

    def test_reversed(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get('/edit/')
        self.assertTrue(response.content.find('Vladimir') > response.content.find('Ganziy'))

    def test_tag(self):
        response = self.client.get('/')
        self.assertNotContains(response, '/admin/contact/person/1/')
        self.client.login(username='admin', password='admin')
        response = self.client.get('/')
        self.assertContains(response, '/admin/contact/person/1/')
