from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render_to_response
from mysite.contact.models import Person


def show_person(request):
    try:
        person = Person.objects.get(last_name="Ganziy")
    except  ObjectDoesNotExist:
        person = None
    except MultipleObjectsReturned:
        person = None

    return render_to_response('base.html', {'person': person})
