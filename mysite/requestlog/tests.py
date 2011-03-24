from django.test import TestCase
from mysite.requestlog.models import RequestLog


class RequestTest(TestCase):

    def test_http(self):
        response = self.client.get('/request/')
        self.failUnlessEqual(response.status_code, 200)
        request = RequestLog.objects.all()
        self.assertNotEqual(request.count, 0)
        request = RequestLog.objects.order_by('-id')[0]
        self.assertContains(response, 'id request ' + str(request.id))
        self.assertContains(response, request.user_ip)
        self.assertContains(response, request.link_come)
        self.assertContains(response, request.user_agent)
        self.assertContains(response, request.host)
