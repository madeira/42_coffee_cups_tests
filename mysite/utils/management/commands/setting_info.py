from django.core.management.base import NoArgsCommand
from django.db.models import get_models


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for model in get_models():
            mod = model.__name__
            obj = model.objects.count()
            info = str(mod) + ' have ' + str(obj) + ' objects' + '\n'
            self.stdout.write(info)
            self.stderr.write("Error: ")
            self.stderr.write(info)
