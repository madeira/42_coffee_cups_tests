from django.shortcuts import render_to_response
from django.template import RequestContext


def show_settings(request):
    return render_to_response('context_processor.html', context_instance=RequestContext(request))
