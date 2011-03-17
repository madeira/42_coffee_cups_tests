from django.shortcuts import render_to_response
from mysite.requestlog.models import RequestLog


def request_list(request):
    request = RequestLog.objects.all().order_by('-id')[:10]
    return render_to_response("request_log.html", {"request": request})
