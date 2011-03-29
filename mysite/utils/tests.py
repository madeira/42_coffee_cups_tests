from django.core.management import call_command
from django.test import TestCase
from django.db.models import get_models
import datetime


class BashTest(TestCase):

    def test_command(self):
        call_command('setting_info', stdout=open('/dev/null', 'w'),
                     stderr=open('%s.dat' % datetime.date.today(), 'w'))
        s = []
        for model in get_models():
            mod = model.__name__
            obj = model.objects.count()
            info = 'Error: ' + str(mod) + ' have ' + str(obj) + ' objects' + '\n'
            s.append(info)

        line = file('%s.dat' % datetime.date.today()).readlines()
        self.assertEqual(s, line)
