from django.shortcuts import render_to_response
from mysite.contact.models import Person


def show_person(request):
    results = {}

    try:
        results['person'] = Person.objects.get(last_name="Ganziy")
    except  (Person.DoesNotExist, Person.MultipleObjectsReturned), e:
        results['error'] = e

    return render_to_response('base.html', results)
