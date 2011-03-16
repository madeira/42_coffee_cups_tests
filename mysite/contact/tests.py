from django.test import TestCase
from mysite.contact.models import Person


class ContactTest(TestCase):
    fixtures=['initial_data.json']

    def setUp(self):
        contact=Person.objects.all()
        self.count=contact.count()
        contact2=Person.objects.filter(last_name="Ganziy")
        self.assertEqual(self.count, contact2.count())

    def test_base(self):
        self.contact=Person.objects.create(first_name="Ivanov",
                                            last_name="Ivan",
                                            mail="ivanov@gmail",
                                            date="1945-01-01")
        contact_count2=Person.objects.all()
        self.assertNotEqual(self.count, contact_count2.count())
        self.contact.delete()
        contact_count2=Person.objects.all()
        self.assertEqual(self.count, contact_count2.count())

    def test_http(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)
        self.assertContains(response, 'Ganziy',
                            count=1, status_code=200, msg_prefix='')
        self.assertContains(response, 'ganziy.vova@gmail.com',
                            count=1, status_code=200, msg_prefix='')
        self.assertTemplateUsed(response, 'base.html', msg_prefix='')
