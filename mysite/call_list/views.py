from django.shortcuts import render_to_response
from mysite.call_list.models import Call_middle


def call_list(request):
    call = Call_middle.objects.all().order_by('-id')[:10]
    return render_to_response("call.html", {"call": call})
