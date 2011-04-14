from django.shortcuts import render_to_response
from mysite.contact.models import Person
from mysite.contact.form import PersonForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.template.loader import render_to_string
from django.http import HttpResponse


def show_person(request):
    results = {}
    request_user = request.user.is_authenticated()

    try:
        results['person'] = Person.objects.get(last_name="Ganziy")
    except  (Person.DoesNotExist, Person.MultipleObjectsReturned), e:
        results['error'] = e

    return render_to_response('base.html', results,
                              RequestContext(request,
                                             {'request_user': request_user}))


@login_required
def edit_person(request):
    if request.is_ajax() and request.method == 'POST':
        form = PersonForm(request.POST,
                          instance=Person.objects.get(last_name="Ganziy"))
        if form.is_valid():
            form.save()
            status = 'valid'
        else:
            status = 'invalid'
        response_text = render_to_string("person_form.html", {'form': form})
        return HttpResponse(simplejson.dumps({'status': status,
                                              'text': response_text}),
                                            mimetype='application/javascript')
    else:
        form = PersonForm(instance=Person.objects.get(last_name="Ganziy"))
    return render_to_response('edit_person.html',
                              RequestContext(request, {'form': form}))
