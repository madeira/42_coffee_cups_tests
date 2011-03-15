from mysite.call_list.models import Call_middle


class  CallMiddleware(object):

    def process_request(self, request):
        call=Call_middle()
        call.user_ip=request.META['REMOTE_ADDR']
        call.link_come=request.META.get('HTTP_REFERER', '')
        call.user_agent=request.META.get('HTTP_USER_AGENT', '')
        call.host=request.META.get('HTTP_HOST', '')
        call.save()
