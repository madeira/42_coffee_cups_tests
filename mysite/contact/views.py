from django.shortcuts import render_to_response
from mysite.contact.models import Person
from django.forms import ModelForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def show_person(request):
    results = {}
    request_user = request.user.is_authenticated()

    try:
        results['person'] = Person.objects.get(last_name="Ganziy")
    except  (Person.DoesNotExist, Person.MultipleObjectsReturned), e:
        results['error'] = e

    return render_to_response('base.html', results,
                              RequestContext(request, {'request_user': request_user}))


class PersonForm(ModelForm):

    class Meta:
        model = Person


@login_required
def edit_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=Person.objects.get(last_name="Ganziy"))
        if form.is_valid():
            form.save()
    else:
        form = PersonForm(instance=Person.objects.get(last_name="Ganziy"))
    return render_to_response('edit_persone.html',
                              RequestContext(request, {'form': form}))
