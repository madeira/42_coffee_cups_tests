from mysite.contact.models import Middlewares


class  CallMiddleware(object):

    def process_request(self, request):
        call=Middlewares()
        call.user_ip=request.META['REMOTE_ADDR']
        call.link_come=request.META['HTTP_REFERER']
        call.user_agent=request.META['HTTP_USER_AGENT']
        call.host=request.META['HTTP_HOST']
        call.save()
