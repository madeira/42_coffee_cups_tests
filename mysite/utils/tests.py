from django.core.management import call_command
from django.test import TestCase
from django.db.models import get_models
from mysite.contact.models import Person
from mysite.utils.models import Signal
import cStringIO


class BashTest(TestCase):

    def test_command(self):
        buf1 = buf2 = err = cStringIO.StringIO()
        call_command('setting_info', stdout=(buf1), stderr=(err))
        for model in get_models():
            mod = model.__name__
            obj = model.objects.count()
            info = str(mod) + ' have ' + str(obj) + ' objects' + '\n'
            buf2.write(info)

        self.assertTrue(buf2.getvalue() in buf1.getvalue())


class SignalTest(TestCase):

    def test_signal(self):
        contact = Person.objects.create(first_name="Up", last_name="Vladimir",
                                        date="1986-09-24", bio="up",
                                        mail="up@up.ru", jabber="up",
                                        skype="up", other="up")
        signal_action = Signal.objects.order_by('-id')
        self.assertEqual(signal_action[0].action, 'create')
        contact.save()
        self.assertEqual(signal_action[0].action, 'edit')
        contact.delete()
        self.assertEqual(signal_action[0].action, 'delete')
