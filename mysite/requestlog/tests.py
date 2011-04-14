from django.conf import settings
from django.test import TestCase
from mysite.requestlog.models import RequestLog
from django.core.urlresolvers import reverse


class RequestTest(TestCase):

    def test_http(self):
        response = self.client.get(reverse('requestlog'))
        self.failUnlessEqual(response.status_code, 200)
        request = RequestLog.objects.all()
        self.assertNotEqual(request.count, 0)
        request = RequestLog.objects.order_by('-id')[0]
        self.assertContains(response, 'id request ' + str(request.id))
        self.assertContains(response, request.user_ip)
        self.assertContains(response, request.link_come)
        self.assertContains(response, request.user_agent)
        self.assertContains(response, request.host)


class RequestPriorityTest(TestCase):

    def test_priority_settings(self):
        self.assertEqual(settings.REQUESTLOG_DEFAULT_PRIORITY, False)

    def test_priority_filters(self):
        self.request = RequestLog.objects.create(priority='True')
        self.request.save
        response = self.client.get(reverse('requestlog_sorting', args=['asc']))
        self.failUnlessEqual(response.status_code, 200)
        self.assertTrue(response.content.find('True')
                        < response.content.find('False'))
        response = self.client.get(reverse('requestlog_sorting',
                                           args=['desc']))
        self.failUnlessEqual(response.status_code, 200)
        self.assertTrue(response.content.find('True') >
                        response.content.find('False'))
        response = self.client.get(reverse('requestlog_filter',
                                           args=['false']))
        self.failUnlessEqual(response.status_code, 200)
        self.assertNotContains(response, 'True')
        response = self.client.get(reverse('requestlog_filter',
                                           args=['true']))
        self.failUnlessEqual(response.status_code, 200)
        self.assertNotContains(response, 'False')
        response = self.client.get(reverse('requestlog'))
        self.assertContains(response, 'False')
        self.assertContains(response, 'True')
