from django import forms
from django.forms.widgets import TextInput
from mysite.contact.models import Person


class CalendarWidget(TextInput):

    class Media:
        js = ("/media/js/jquery-1.5.1.min.js",
              "/media/js/jquery.datepick.js")
        css = {"all":
               ("/media/css/jquery.datepick.css", )}


class PersonForm(forms.ModelForm):
    date = forms.DateField(widget=CalendarWidget)

    class Meta:
        model = Person
