from django.shortcuts import render_to_response
from mysite.requestlog.models import RequestLog


def request_list(request):
    request = RequestLog.objects.all().order_by('-id')[:10]
    return render_to_response("request_log.html", {"request": request})


def request_asc_desc_priority(request, offset):
    if offset == 'asc':
            request = RequestLog.objects.filter(priority=True)\
                      .order_by('-id')[:5]
            request2 = RequestLog.objects.filter(priority=False)\
                       .order_by('-id')[:5]
    else:
            request = RequestLog.objects.filter(priority=False)\
                      .order_by('-id')[:5]
            request2 = RequestLog.objects.filter(priority=True)\
                       .order_by('-id')[:5]
    return render_to_response("request_log.html", {"request2": request2,
                                                           "request": request})


def request_true_false_priority(request, offset):
    if offset == 'true':
        request = RequestLog.objects.filter(priority=True)\
                  .order_by('-id')[:10]
    else:
        request = RequestLog.objects.filter(priority=False)\
                  .order_by('-id')[:10]
    return render_to_response("request_log.html", {"request": request})
