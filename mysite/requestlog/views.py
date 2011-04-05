from django.shortcuts import render_to_response
from mysite.requestlog.models import RequestLog


def request_list(request):
    request = RequestLog.objects.all().order_by('-id')[:10]
    return render_to_response("request_log.html", {"request": request})


def request_true_priority(request):
    request = RequestLog.objects.filter(priority=True).order_by('-id')[:10]
    return render_to_response("request_log.html", {"request": request})


def request_false_priority(request):
    request = RequestLog.objects.filter(priority=False).order_by('-id')[:10]
    return render_to_response("request_log.html", {"request": request})


def request_asc_priority(request):
    request = RequestLog.objects.filter(priority=True).order_by('-id')[:5]
    request2 = RequestLog.objects.filter(priority=False).order_by('-id')[:5]
    return render_to_response("request_log.html", {"request": request, "request2": request2})


def request_desc_priority(request):
    request3 = RequestLog.objects.filter(priority=True).order_by('-id')[:5]
    request2 = RequestLog.objects.filter(priority=False).order_by('-id')[:5]
    return render_to_response("request_log.html", {"request2": request2, "request3": request3})
