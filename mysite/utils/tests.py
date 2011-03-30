from django.core.management import call_command
from django.test import TestCase
from django.db.models import get_models
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
