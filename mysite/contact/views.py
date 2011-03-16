from django.shortcuts import render_to_response
from mysite.contact.models import Person


def show_person(request):
    person=Person.objects.get(last_name='Ganziy')
    return render_to_response('base.html', {'person': person})
