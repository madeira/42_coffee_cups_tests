from django.shortcuts import render_to_response
from mysite.contact.models import Person


def show_person(request):
    person=Person.objects.filter(last_name="Ganziy")
    if person.count() == 1:
        person=Person.objects.get(last_name="Ganziy")
        return render_to_response('base.html', {'person': person})
    elif person.count() >= 1:
        count=person.count()
        return render_to_response('person_error.html', {'count': count})
    else:
        return render_to_response('person_error_none.html', )
