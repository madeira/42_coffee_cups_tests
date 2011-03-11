from django.shortcuts import render_to_response
from mysite.contact.models import Persone


def show_persone(request):
    persone=Persone.objects.get(last_name='Ganziy')
    return render_to_response('persone.html', {'persone': persone})
