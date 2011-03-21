from mysite.requestlog.models import RequestLog


class  RequestMiddleware(object):

    def process_request(self, request):
        call = RequestLog()
        call.user_ip = request.META['REMOTE_ADDR']
        call.link_come = request.META.get('HTTP_REFERER', '')
        call.user_agent = request.META.get('HTTP_USER_AGENT', '')
        call.host = request.META.get('HTTP_HOST', '')
        call.save()
